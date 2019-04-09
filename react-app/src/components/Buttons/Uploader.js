import React, { Component } from "react";
import styled from "styled-components";

const Container = styled.div`
  margin-top: 1rem;
  position: relative;
  overflow: hidden;
  display: inline-block;

  [type="file"] {
    position: absolute;
    height: 100%;
    overflow: hidden;
    width: 100%;
    left: 0;
    top: 0;
    opacity: 0;
    cursor: pointer;
  }

  label {
    font-size: 11px;
  }

  div.wrapper {
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

  div.wrapper:hover {
    border-radius: 6px;
    background-color: ${props => props.theme.darkergrey};
  }

  div.wrapper:active {
    border-radius: 6px;
    background-color: ${props => props.theme.darkestgrey};
  }

  div.wrapper:focus {
    border-radius: 6px;
    box-shadow: 0 0 0 2px ${props => props.theme.darkestgrey};
  }
`;

class Uploader extends Component {
  constructor(props) {
    super(props);
    this.uploadFile = this.uploadFile.bind(this);
  }

  uploadFile = () => {
    const data = new FormData();
    data.append("file", this.uploadInput.files[0]);

    fetch("http://localhost:5000/upload-inputs", {
      method: "POST",
      body: data
    }).then(response => {
      this.uploadInput.value = "";
      if (response.statusText === "OK") {
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
          <div className="wrapper">
            <label htmlFor="file">Upload Term (CSV)</label>
            <input
              ref={ref => {
                this.uploadInput = ref;
              }}
              type="file"
              accept=".csv"
              onChange={this.uploadFile}
            />
          </div>
        </Container>
      </React.Fragment>
    );
  }
}

export default Uploader;
