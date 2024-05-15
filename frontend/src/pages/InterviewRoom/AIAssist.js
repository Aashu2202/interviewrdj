

// import React, { useState } from "react";
// import axios from "axios";
// import "./aiassist.css";
// import InterviewRoom from "./InterviewRoom";
// import AIimg from "../../assets/images/GIFvoiceassistant.gif";

// const AIAssist = () => {
//   const [recordingInProgress, setRecordingInProgress] = useState(false); // Track whether recording is in progress
//   const [buttonClicked, setButtonClicked] = useState(false); // Track whether the button has been clicked
//   const name = localStorage.getItem("name");
//   const email = localStorage.getItem("useremail");
//   const phone = localStorage.getItem("phone");

//   const startInterview = async () => {
//     try {
//       if (!buttonClicked) {
//         // Disable the button to prevent multiple clicks
//         setButtonClicked(true);

//         // Start recording when starting the interview
//         startRecording();

//         const formData = {
//           value: true,
//         };

//         const res = await axios.post(
//           "http://localhost:8000/api/start-interview/",
//           formData
//         );
//         const data = res.data;
//         console.log(data);
//         if (data.call === true) {
//           // If response from backend is true, stop recording and submit
//           stopRecordingAndSubmit();
//         }
//       }
//     } catch (error) {
//       console.error("Error starting interview:", error);
//     }
//   };

//   const startRecording = () => {
//     // Logic to start recording
//     setRecordingInProgress(true);
//   };

//   const stopRecordingAndSubmit = async () => {
//     // Logic to stop recording and submit
//     setRecordingInProgress(false);
//   };

//   return (
//     <>
//       <div className="col-12 AIpage">
//         <div className="container">
//           <div className="row justify-content-center align-items-center">
//             <div className="col-lg-6 col-12">
//               <div className="cam-recorder">
//                 <InterviewRoom recordingInProgress={recordingInProgress} />
//               </div>
//             </div>
//             <div className="col-lg-6 col-12">
//               <div>
//                 <div className="ai-img">
//                   <img src={AIimg} className="img-fluid w-100 h-100" />
//                 </div>
//               </div>
//             </div>
//             <div className="col-12 text-center">
//               <button
//                 className="btn btn-primary"
//                 onClick={startInterview}
//                 disabled={buttonClicked} // Disable the button if it's already clicked
//               >
//                 Start Interview
//               </button>
//             </div>
//           </div>
//           <div className="row justify-content-center align-items-center">
//             <div className="col-lg-6 userdetails">
//               <span className="d-block">{name}</span>
//               <span className="d-block">{email}</span>
//               <span className="d-block">{phone}</span>
//             </div>
//             <div className="col-lg-6"></div>
//           </div>
//         </div>
//       </div>
//     </>
//   );
// };

// export default AIAssist;