import React, { Component } from "react";
import styled from "styled-components";

const FlexContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
`;

const FlexChild = styled.div`
  width: 100%;
`;

const StyledSelect = styled.select`
  line-height: 1.3;
  padding: 0.8em;
  max-width: 100%;
  box-sizing: border-box;
  margin: 1em 0;
  border: 1px solid #aaa;
  box-shadow: 0 1px 0 1px rgba(0, 0, 0, 0.04);
  border-radius: 0.5em;
  -moz-appearance: none;
  -webkit-appearance: none;
  appearance: none;
  background-color: #fff;
  background-image: linear-gradient(to bottom, #ffffff 0%, #e5e5e5 100%);

  ::-ms-expand {
    display: none;
  }
  :hover {
    border-color: #888;
  }
  :focus {
    border-color: #aaa;
    box-shadow: 0 0 1px 3px rgba(59, 153, 252, 0.7);
    box-shadow: 0 0 0 3px -moz-mac-focusring;
    color: #222;
    outline: none;
  }
`;

const StyledInput = styled.textarea`
  width: 100%;
  margin: 1em 0;
`;

class Error extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dayOptions: [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ],
      timeOptions: [
        "8:00AM",
        "8:30AM",
        "9:00AM",
        "9:30AM",
        "10:00AM",
        "10:30AM",
        "11:00AM",
        "11:30AM",
        "12:00PM",
        "12:30PM",
        "1:00PM",
        "1:30PM",
        "2:00PM",
        "2:30PM",
        "3:00PM",
        "3:30PM",
        "4:00PM",
        "4:30PM",
        "5:00PM",
        "5:30PM",
        "6:00PM",
        "6:30PM"
      ],
      startTime: "",
      endTime: "",
      daySelect: ""
    };
    this.onSelectStartChange = this.onSelectStartChange.bind(this);
    this.onSelectEndChange = this.onSelectEndChange.bind(this);
  }

  onSelectDayChange = e => {
    this.setState({ daySelect: e.target.value });
  };

  onSelectStartChange = e => {
    this.setState({ startTime: e.target.value });
  };

  onSelectEndChange = e => {
    this.setState({ endTime: e.target.value });
  };

  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          <FlexChild>
            <p>Day:</p>
            <StyledSelect onChange={this.onSelectDayChange}>
              {this.state.dayOptions.map(dayOption => (
                <option value={dayOption}>{dayOption}</option>
              ))}
            </StyledSelect>
          </FlexChild>
          <FlexChild>
            <p>Start Time:</p>
            <StyledSelect onChange={this.onSelectStartChange}>
              {this.state.timeOptions.map(timeOption => (
                <option value={timeOption}>{timeOption}</option>
              ))}
            </StyledSelect>
          </FlexChild>
          <FlexChild>
            <p>End Time:</p>
            <StyledSelect onChange={this.onSelectEndChange}>
              {this.state.timeOptions.map(timeOption => (
                <option value={timeOption}>{timeOption}</option>
              ))}
            </StyledSelect>
          </FlexChild>
          <FlexChild>
            <p>Reasons:</p>
            <StyledInput name="Reasons" rows="4" />
          </FlexChild>
          <FlexChild>
            <p>
              Selected Day: {this.state.daySelect}, Start Time:
              {this.state.startTime}, End Time: {this.state.endTime}
            </p>
          </FlexChild>
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default Error;
