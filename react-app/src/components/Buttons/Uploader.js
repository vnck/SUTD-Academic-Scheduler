import React, { Component } from "react";
import styled from "styled-components";

const Container = styled.div`
  margin-top: 1rem;

  button {
    padding: 1rem;
    border: none;
    text-align: center;
    text-decoration: none;
    background-color: ${props => props.theme.grey};
    font-weight: 600;
    border-radius: 6px;
    outline: none;
    cursor: pointer;
  }

  button:hover {
    background-color: ${props => props.theme.darkergrey};
  }

  button:active {
    background-color: ${props => props.theme.darkestgrey};
  }

  button:focus {
    box-shadow: 0 0 0 2px ${props => props.theme.darkestgrey};
  }
`;

class Uploader extends Component {
  constructor(props) {
    super(props);
    this.uploadFile = this.uploadFile.bind(this);
  }

  uploadFile = e => {
    e.preventDefault();

    const data = new FormData();
    data.append("file", this.upload.files[0]);

    fetch("http://localhost:5000/upload-inputs", {
      method: "POST",
      body: data
    }).then(response => {
      if (response === 1) {
        alert("File uploaded succesfully");
      } else {
        alert("File failed to upload");
      }
    });
  };

  render() {
    return (
      <React.Fragment>
        <Container>
          <input
            ref={ref => {
              this.uploadInput = ref;
            }}
            type="file"
          />
          <button type="button" onClick={this.uploadeFile}>
            Upload Term Outline (CSV)
          </button>
        </Container>
      </React.Fragment>
    );
  }
}

export default Uploader;
