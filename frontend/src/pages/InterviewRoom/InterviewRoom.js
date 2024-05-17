import React, { useRef, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify"; // Import toast from react-toastify
import "react-toastify/dist/ReactToastify.css"; // Import toast styles
import RecordRTC from "recordrtc";
import axios from "axios";
import * as blazeface from "@tensorflow-models/blazeface"; // Face detection model
import * as cocoSsd from "@tensorflow-models/coco-ssd"; // Object detection model
import * as tf from "@tensorflow/tfjs"; // Import TensorFlow.js
const URL = process.env.REACT_APP_BACKEND_URL + "/api/video";
const InterviewRoom = ({ recordingInProgress }) => {
  let navigate = useNavigate();
  const webcamRef = useRef(null);
  const mediaRecorderRef = useRef(null);
  const [recording, setRecording] = useState(false);
  const [timer, setTimer] = useState(0);
  const [noFaceWarning, setNoFaceWarning] = useState(false);
  const [gadgetWarning, setGadgetWarning] = useState(false);
  const [multipleFacesWarning, setMultipleFacesWarning] = useState(false);
  const [isMounted, setIsMounted] = useState(true); // Flag to track component mount state

  useEffect(() => {
    async function initializeModels() {
      try {
        await Promise.all([
          blazeface.load(),
          cocoSsd.load(),
          tf.setBackend("webgl"),
        ]);
        console.log("Models and WebGL backend initialized");
      } catch (error) {
        console.error("Error initializing models and WebGL backend:", error);
      }
    }
    initializeModels();

    // Cleanup function to set isMounted to false when component unmounts
    return () => {
      setIsMounted(false);
    };
  }, []);

  useEffect(() => {
    if (recordingInProgress) {
      startRecording();
    } else {
      stopRecordingAndSubmit();
    }
  }, [recordingInProgress]);

  const detectFacesAndObjects = async () => {
    const faceModel = await blazeface.load();
    const objectModel = await cocoSsd.load();

    const checkForFacesAndObjects = async () => {
      if (webcamRef.current && webcamRef.current.readyState === 4) {
        try {
          const videoElement = webcamRef.current;
          const tensor = tf.browser.fromPixels(videoElement);
          
          // Detect faces
          const facePredictions = await faceModel.estimateFaces(tensor);

          // Detect electronic gadgets
          const objectPredictions = await objectModel.detect(tensor);
          let gadgetsFound = false;
          let multipleFacesFound = false;

          if (facePredictions.length > 1) {
            multipleFacesFound = true;
          }
          objectPredictions.forEach((prediction) => {
            const label = prediction.class.toLowerCase();
            if (["cell phone", "laptop", "tablet"].includes(label)) {
              gadgetsFound = true;
            }
          });

          // Set warnings based on detections
          setNoFaceWarning(facePredictions.length === 0);
          setGadgetWarning(gadgetsFound);
          setMultipleFacesWarning(multipleFacesFound);

          // Show toast if multiple faces and electronic gadgets are detected
          if (multipleFacesFound && gadgetsFound) {
            console.log("Multiple faces and electronic gadgets detected!");
            toast.warn("Multiple faces and electronic gadgets detected!", {
              autoClose: 5000, // Close toast after 5 seconds
            });
          }
        } catch (error) {
          console.error("Error detecting faces and objects:", error);
        }
      } else {
        // Handle cases where webcamRef.current is not ready
        console.warn("Webcam is not ready.");
      }

      // Request next animation frame only if component is still mounted
      if (isMounted) {
        requestAnimationFrame(checkForFacesAndObjects);
      }
    };

    checkForFacesAndObjects();
  };

  const startRecording = () => {
    navigator.mediaDevices
      .getUserMedia({ video: true, audio: { echoCancellation: true, autoGainControl: true } })
      .then((stream) => {
        const recorder = RecordRTC(stream, { type: "video" });
        recorder.startRecording();
        mediaRecorderRef.current = recorder;
        setRecording(true);
        setTimer(0); // Reset timer when recording starts
        webcamRef.current.srcObject = stream; // Set webcam stream to the video element
        detectFacesAndObjects();
      })
      .catch((error) => {
        console.error("Error starting recording:", error);
      });
  };

  const stopRecordingAndSubmit = async () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stopRecording(async () => {
        const blob = mediaRecorderRef.current.getBlob();
        const formData = new FormData();
        formData.append("video", blob, "recorded_video.webm");
        const userEmail = localStorage.getItem("useremail");
        formData.append("email", userEmail);

        try {
          const response = await axios.post(
            URL,
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
          );

          if (response.status === 200 || response.status === 201) {
            console.log("Video uploaded successfully");
            const streamTracks = webcamRef.current.srcObject.getTracks();
            streamTracks.forEach((track) => track.stop());
            navigate("/success");
          } else {
            console.error("Failed to upload video:", response.statusText);
          }
        } catch (error) {
          console.error("Error uploading video:", error.message);
        }

        setRecording(false);
      });
    }
  };

  return (
    <div className="col-12 webcamera">
      <video ref={webcamRef} autoPlay muted className="video-cam" />
      {recording && (
        <div className="recording">
          Recording: {Math.floor(timer / 60)}:
          {(timer % 60).toLocaleString("en-US", { minimumIntegerDigits: 2 })}
        </div>
      )}
      {noFaceWarning && (
        <div style={{ color: "red", fontWeight: "bold" }}>
          Warning: No face detected!
        </div>
      )}
      {gadgetWarning && (
        <div style={{ color: "orange", fontWeight: "bold" }}>
          Warning: Electronic gadget detected!
        </div>
      )}
      {multipleFacesWarning && (
        <div style={{ color: "yellow", fontWeight: "bold" }}>
          Warning: Multiple faces detected!
        </div>
      )}
    </div>
  );
};

export default InterviewRoom;
