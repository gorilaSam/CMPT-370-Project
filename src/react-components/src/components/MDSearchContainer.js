import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import PatientProfileContainer from './PatientProfileContainer';

function MDSearch(props) {
    const [specialty, setSpecialty] = useState("");
    const [doctor, setDoctor] = useState("");
    const [specialtySelected, setSpecialtySelected] = useState(false);
    const [doctorSelected, setDoctorSelected] = useState(false);
    // need to change to get selected instead of checking if it was selected
    if (doctorSelected) {
        return <RequestForm doctorName={doctor} doctorSpecialty={specialty}/>
    }
    else if (specialtySelected) {
        return <DoctorList setDoctor={setDoctor} setSelected={setDoctorSelected}/>
    }
    else {
        return <SpecialtyList setSpecialty={setSpecialty} setSelected={setSpecialtySelected}/>
    }
}

function SpecialtyList(props) {
    const [specialty, setSpecialty] = useState('');

    function changeSpecialty(event) {
        const {value} = event.target;
        setSpecialty(value);
    }

    return (
        <div className="homeContainer">
            <PatientProfileContainer/>
            <br />
            <form style={{height: "200px"}}>
                <select className="navBarButton" onChange={changeSpecialty}
                style={{border: "1px solid black"}}>
                    <option selected disabled>-- Select Specialty --</option>
                    <option value="Cardiac">Cardiac</option>
                    <option value="Endocrinologist">Endocrinologist</option>
                    <option value="Oncology">Oncology</option>
                    <option value="Orthopedics">Orthopedics</option>
                    <option value="Urology">Urology</option>
                </select>
                <br /><br />
                <button className="navBarButton" onClick={() => {
                    props.setSpecialty(specialty);
                    props.setSelected(true);
                }}>Search</button>
            </form>
        </div>
    )
}

function DoctorList(props) {
    const [doctor, setDoctor] = useState('');

    function changeDoctor(event) {
        const {value} = event.target;
        setDoctor(value);
    }
    return (
        <div className="homeContainer">
            <PatientProfileContainer />
            <br />
            <form style={{height: "200px"}}>
                <select className="navBarButton" onChange={changeDoctor}
                style={{border: "1px solid black"}}>
                    <option selected disabled>-- Choose Doctor --</option>
                    <option value="Doctor X">Dr. X</option>
                    <option value="Doctor Y">Dr. Y</option>
                    <option value="Doctor Z">Dr. Z</option>
                    <option value="Doctor $">Dr. $</option>
                    <option value="Doctor :)">Dr. :)</option>
                </select>
                <br /><br />
                <button className="navBarButton" onClick={() => {
                    props.setDoctor(doctor);
                    props.setSelected(true);
                }}>Search</button>
            </form>
        </div>
    )
}

function RequestForm(props) {
    return (
        <div className="homeContainer">
            <PatientProfileContainer />
            <h1>{props.doctorName}</h1>
            <h2>Specialty: {props.doctorSpecialty}</h2>
            <br />
            <form style={{height: "550px"}}>
                <textarea
                placeholder="Reason for request"
                style={{width:"70%", height: "450px", fontSize: "24px"}}
                >
                </textarea>
                <br />
                <div className="horizontalDivider" style={{width: "55%"}}/>
                <Link to="/">
                    <button className="navBarButton"
                    style={{marginTop: "5px"}} 
                    >Request</button>
                </Link>
            </form>
        </div>
    )
}

export default MDSearch;