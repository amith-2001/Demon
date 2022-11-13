import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import './App.css';
import Map from './components/Map';
import Data from './components/Data';
import Login from './components/Login';
import logo from './assets/favicon.png'

function App() {
  const username="Dark Pegasus"
  return (
    <React.Fragment>
    <nav className=" box-shadow navbar navbar-expand-lg navbar-light bg-light justify-content-between">
      <div style={{display:'flex',alignItems:'center'}}>
        <a className='navbar-brand'><img className='logo' src={logo}></img></a>
      {/* <span className='display-4'>DE</span>forestation<br/><span className='display-4'>MON</span>itoring<br/><span className='display-4'>S</span>ystem */}
      </div>
      <div className='m-5'>
        <h4>{username}</h4>
      </div>
    </nav>
    {username?
    <div>
      <div className='row justify-content-center d-flex my-5'>
        <div className='col-sm-6 justify-content-center d-flex bg-dark'>
          <Map  status={[0,1,2]}/>
        </div>
      </div>
      <div className='row justify-content-center d-flex my-5'>
        <div className='col-sm-6 justify-content-center d-flex'>
          <Data active={3} inactive={0} sus ={0}/>
        </div>
      </div>
  </div>:<Login/>
}
  </React.Fragment>
  );
}

export default App;
