import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import PatientProfileContainer from './PatientProfileContainer';

function NewNote(props) {
    const [noteText, setNoteText] = useState("");
    const [diagnosisText, setDiagnosisText] = useState("");

    function changeNote(event) {
        const {value} = event.target;
        setNoteText(value)
    }

    function changeDiagnosis(event) {
        const {value} = event.target;
        setDiagnosisText(value);
    }

    return (
        <div  className="homeContainer">
            <PatientProfileContainer/>
            <form style={{height: "600px"}}>
                <br />
                <textarea
                placeholder="Insert Text" value={noteText} onChange={changeNote}
                style={{width:"900px", height: "450px", fontSize: "24px"}}
                >
                </textarea>
                <br />
                <input type="text" placeholder="Diagnosis" value={diagnosisText} onChange={changeDiagnosis}
                style={{width:"450px", fontSize: "16px"}}
                >
                </input>
                <div className="horizontalDivider" style={{width: "450px"}}/>
                <br/>
                <Link to="/">
                    <button className="navBarButton"
                    style={{marginTop: "5px"}} 
                    >Post</button>
                </Link>
                <div className="horizontalDivider" style={{width: "830px"}}/>
            </form>
        </div>
    )
}

// class NewNote extends React.Component {
//     constructor(props) {
//         super();
//         this.state={
//             noteText: "",
//             diagnosisText: ""
//         };
//         this.handleChange = this.handleChange.bind(this);
//     }

//     handleChange(event) {
//         const {name, value} = event.target;
//         this.setState({[name]: value})
//     }

//     render() {
//         return (
//             <div>
//                 <form className="homeContainer" style={{padding: "50px"}}>
//                     <span style={{marginRight: "700px", fontSize: "24px", fontWeight: "bold", fontStyle: "italic"}}>New Note:</span>
//                     <Link to="/">
//                         <button className="navBarButton">Back</button>
//                     </Link>
//                     <br/>
//                     <textarea
//                     placeholder="Insert Text"
//                     name="noteText" 
//                     value={this.state.noteText}
//                     onChange={this.handleChange}
//                     style={{width:"900px", height: "450px", fontSize: "24px"}}
//                     >
//                     </textarea>
//                     <br />
//                     <input
//                     type="text" 
//                     placeholder="Diagnosis"
//                     name="diagnosisText"
//                     value={this.state.diagnosisText}
//                     onChange={this.handleChange}
//                     style={{width:"450px", fontSize: "16px", marginRight: "450px"}}
//                     >
//                     </input>
//                     <br/>
//                     <Link to="/">
//                         <button style={{marginRight: "850px", marginTop: "20px"}} className="navBarButton">Post</button>
//                     </Link>
                    
//                 </form>
//             </div>
//         )
//     }
// }

export default NewNote;