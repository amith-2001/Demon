import { useState } from "react"
export default function Login()
{
    const [incorrect,setincorrect] = useState(0);
    return(<div className="m-5">
        <div className="container">
            <div className="row h-100 d-flex justify-content-center align-items-center">
                <div className="col-sm-6">
                    <div className="card box-shadow">
                        <div className="card-body m-5">
                    <div className="container">
                        <div className="text-center my-5"><h1 className="display-5">Sign in</h1></div>
                        <div className="row my-4 d-flex justify-content-center">
                            <div className="col-sm-8">
                            <input type='text' placeholder="Username" className="form-control"></input>
                            </div>
                        </div>
                        <div className="row my-4 d-flex justify-content-center">
                            <div className="col-sm-8">
                            <input type='password' placeholder="Password" className="form-control"></input>
                            </div>
                        </div>
                        {incorrect?<div className="row justify-content-center d-flex my-2">
                            <div className="text-danger text-center">Incorrect Password/Username</div>
                        </div>:<></>}
                        <div className="row justify-content-center d-flex my-5">
                            <div className="btn btn-success col-sm-6">Login</div>
                        </div>
                    </div>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>)
}