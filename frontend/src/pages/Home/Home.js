import React from 'react';
import { Link } from 'react-router-dom';
import './home.css';

function Home() {
    return (
        <>
            <div className='col-12 background herosection pt-5'>
                <div className='container'>
                    <div className='row justify-content-center align-items-center'>
                        <div className='col-12 text-center mt-5'>
                            <div className='mb-5'>
                                <h1 className='secondarycolor'>Interview <span className='text-gradient'>Warmup</span></h1>
                            </div>
                            <div className='primarycolor mb-5'>
                                <h5>A quick way to  prepare for your next interview  in </h5>
                                <h5>Various Fields</h5>
                                <h5>Practice key questions  , get insights about your answers and get more comfortable interviewings</h5>
                            </div>
                            <div>
                                <Link to={'/login'}>
                                    <button className='btn btn-primary'>Start Practicing <i class='bx bx-right-arrow-alt icon'></i></button>
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Home
