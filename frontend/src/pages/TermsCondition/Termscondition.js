import React from "react";
import { useState } from "react";
import './termcondition.css'
import { Link } from "react-router-dom";
const Termscondition = () => {
  const [isChecked, setIsChecked] = useState(false);
  const [isButtonEnabled, setIsButtonEnabled] = useState(false); // State to manage button enable/disable

  const handleCheckboxChange = (event) => {
    setIsChecked(event.target.checked);
    setIsButtonEnabled(event.target.checked); // Update button state when checkbox is changed
  };
  return (
    <>
      <div className="col-12 background-terms">
        <div className="container">
          <div className="row justify-content-center align-items-center">
            <div className="col-lg-8 col-12">
              <div className="terms p-5 my-4">
                <h5 className="card-title mb-2">Terms & Condition</h5>
                <div className="card-body">
                  <li>
                    By accessing or using our platform, you agree to be bound by
                    these Terms. If you do not agree to these Terms,
                  </li>
                  <ul>
                    <li>Information We Collect</li>
                    <li>
                      <strong>Accurate Information: </strong> You agree to provide
                      accurate and complete information when registering for an
                      account. You are responsible for maintaining the
                      confidentiality of your account credentials.
                    </li>
                    <li>
                      <strong>Interview Duration: </strong>Each interview session
                      has a maximum duration of 30 minutes, during which all test
                      components must be completed.
                    </li>
                    <li>
                      <strong>Test Integrity: </strong> Users are prohibited from
                      engaging in any form of cheating or dishonest behavior
                      during interview sessions. Any such behavior may result in
                      the termination of the session and disciplinary action.
                    </li>
                    <li>
                      <strong>Suspension or Termination:</strong>We reserve the
                      right to suspend or terminate your access to our platform at
                      any time for any reason, including but not limited to
                      violation of these Terms or abuse of our platform.
                    </li>
                    <li>
                      <strong>Effect of Termination:</strong>Upon termination,
                      your account and access to the platform will be disabled,
                      and any remaining interview credits or subscriptions may be
                      forfeited.
                    </li>

                  </ul>
                </div>
                <h5 className="card-title text-center mt-4 mb-2">Privacy Policy</h5>
                <div className="card-body">
                  <p>
                    This Privacy Policy outlines how we collect, use, and protect
                    your personal information when you use our platform.
                  </p>
                  <ul>
                    <li>Information We Collect</li>
                    <li>
                      <strong>Account Information: </strong> When you sign up for
                      an account, we collect your name, email address, and other
                      information you provide.
                    </li>
                    <li>
                      <strong>Interview Data: </strong> We collect information
                      related to interviews conducted on our platform, including
                      candidate resumes, interview questions, responses, and
                      feedback.
                    </li>
                    <li>
                      <strong>Usage Data: </strong>We automatically collect
                      information about your use of the Service, such as log data,
                      device information, and IP addresses.{" "}
                    </li>

                    <li>

                      <strong>How We Use Your Information</strong>
                      We may use the information we collect for the following
                      purposes:
                    </li>
                    <li>To provide and maintain the Service.</li>
                    <li>
                      To personalize your experience and improve our services.
                    </li>
                    <li>
                      To communicate with you, including responding to your
                      inquiries and providing customer support.
                    </li>
                    <li>
                      To analyze usage trends and optimize the performance of the
                      platform.
                    </li>
                    <li>
                      To comply with legal obligations and enforce our policies.
                    </li>
                    <li>
                      <strong>Contact Us</strong>
                    </li>
                    <li>
                      If you have any questions or concerns about our Privacy
                      Policy, please contact us at [contact email].
                    </li>

                  </ul>
                </div>
                <div className="mt-3">
                  <input
                    type="checkbox"
                    id="remember"
                    class="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded focus:ring-purple-500 dark:focus:ring-purple-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                    onChange={handleCheckboxChange}
                  />
                  <label htmlFor="remember" className=" remenber-link ms-3" >
                    I have read and agree to the Terms and Conditions
                  </label>
                  <div className="btn-class mt-3">
                    <Link to={"/aiassist"}>
                      <button
                        type="submit"
                        class={`focus:outline-none text-white bg-purple-600 hover:bg-purple-700 focus:ring-4 focus:ring-purple-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-purple-500 dark:hover:bg-purple-600 dark:focus:ring-purple-800 ${!isButtonEnabled && 'opacity-50 cursor-not-allowed'}`}
                        disabled={!isButtonEnabled}
                      >
                        Next
                      </button>
                    </Link>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Termscondition;