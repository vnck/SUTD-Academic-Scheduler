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
  justify-content: right;
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

// const TabContainer = styled.div`
//   width: 100%;
//   display: flex;
//   justify-content: center;
//   margin-bottom: 1rem;
// `;

// const TabButton = styled.div`
//   width: 100%;
//   text-align: center;
//   padding: 0.4rem 1rem;
//   border: none;
//   background-color: ${props =>
//     props.weekly ? props.theme.accent : props.theme.grey};
//   color: ${props => props.theme.white};
//   cursor: pointer;

//   :hover {
//     background-color: ${props => props.theme.accentdark};
//   }

//   :active {
//     background-color: ${props => props.theme.accentdark};
//   }

//   :focus {
//     box-shadow: 0 0 0 2px ${props => props.theme.accentdark};
//   }
// `;

const StyledButton = styled.button`
  padding: 1rem;
  border: none;
  text-align: center;
  text-decoration: none;
  background-color: ${props => props.theme.grey};
  font-weight: 600;
  border-radius: 6px;
  outline: none;
  cursor: pointer;

  :hover:enabled {
    background-color: ${props => props.theme.darkergrey};
  }

  :active:enabled {
    background-color: ${props => props.theme.darkestgrey};
  }

  :disabled {
    color: ${props => props.theme.darkestgrey};
  }

  :focus:enabled {
    box-shadow: 0 0 0 2px ${props => props.theme.darkestgrey};
  }
`;

class PreferenceForm extends Component {
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
      weekOptions: [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14"
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
      weekly: true,
      startTime: "Monday",
      endTime: "8:00AM",
      daySelect: "8:00AM",
      weekSelect: "1",
      reason: ""
    };
    this.onSelectDayChange = this.onSelectDayChange.bind(this);
    this.onSelectDayChange = this.onSelectDayChange.bind(this);
    this.onSelectStartChange = this.onSelectStartChange.bind(this);
    this.onSelectEndChange = this.onSelectEndChange.bind(this);
    this.onSelectWeekly = this.onSelectWeekly.bind(this);
    this.onNotSelectWeekly = this.onNotSelectWeekly.bind(this);
    this.updateReason = this.updateReason.bind(this);
    this.checkSubmit = this.checkSubmit.bind(this);
  }

  onSelectWeekly = () => {
    this.setState({ weekly: true });
  };

  onNotSelectWeekly = () => {
    this.setState({ weekly: false });
  };

  onSelectDayChange = e => {
    this.setState({ daySelect: e.target.value });
  };

  onSelectWeekChange = e => {
    this.setState({ weekSelect: e.target.value });
  };

  onSelectStartChange = e => {
    this.setState({ startTime: e.target.value });
  };

  onSelectEndChange = e => {
    this.setState({ endTime: e.target.value });
  };

  updateReason = e => {
    this.setState({ reason: e.target.value });
  };

  checkSubmit = () => {
    return this.state.reason === "";
  };

  submitRequest = e => {
    e.preventDefault();
    var that = this;
    try {
      // authentication API
      fetch("http://localhost:5000/add-request", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          weekly: that.state.weekly,
          startTime: that.state.startTime,
          endTime: that.state.endTime,
          daySelect: that.state.daySelect
        })
      })
        .then(response => {
          return response.json();
        })
        .then(data => alert(data));
    } catch (e) {
      alert(e);
    }
    this.props.handler();
  };

  render() {
    return (
      <React.Fragment>
        <FlexContainer>
          <FlexContainer>
            <p style={{ "margin-bottom": "1rem", "font-weight": "600" }}>
              Add Schedule Block
            </p>
          </FlexContainer>
          {/* <TabContainer>
            <TabButton weekly={this.state.weekly} onClick={this.onSelectWeekly}>
              Day
            </TabButton>
            <TabButton
              weekly={!this.state.weekly}
              onClick={this.onNotSelectWeekly}
            >
              Date
            </TabButton>
          </TabContainer>
          <FlexContainer>
            {this.state.weekly && (
              <FlexChild>
                <p>Day:</p>
                <StyledSelect onChange={this.onSelectDayChange}>
                  {this.state.dayOptions.map(dayOption => (
                    <option value={dayOption}>{dayOption}</option>
                  ))}
                </StyledSelect>
              </FlexChild>
            )}
            {!this.state.weekly && (
              <FlexChild>
                <p>Week:</p>
                <StyledSelect onChange={this.onSelectWeekChange}>
                  {this.state.weekOptions.map(weekOption => (
                    <option value={weekOption}>{weekOption}</option>
                  ))}
                </StyledSelect>
                <p>Day:</p>
                <StyledSelect onChange={this.onSelectDayChange}>
                  {this.state.dayOptions.map(dayOption => (
                    <option value={dayOption}>{dayOption}</option>
                  ))}
                </StyledSelect>
              </FlexChild>
            )} */}
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
              <StyledInput
                style={{ width: "24rem" }}
                type="text"
                value={this.state.reason}
                onChange={this.updateReason}
                name="Reasons"
                rows="4"
              />
            </FlexChild>
            <FlexChild>
              <StyledButton
                disabled={this.checkSubmit()}
                onClick={this.submitRequest}
              >
                Submit
              </StyledButton>
            </FlexChild>
          </FlexContainer>
        </FlexContainer>
      </React.Fragment>
    );
  }
}

export default PreferenceForm;
