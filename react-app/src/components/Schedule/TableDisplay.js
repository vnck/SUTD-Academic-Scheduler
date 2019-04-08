import React, { Component } from "react";
import styled from "styled-components";
import DayCol from "./DayCol";

const DayHeader = styled.div`
  background-color: ${props => props.theme.white};
  border: 1px solid ${props => props.theme.darkestgrey};
  text-align: center;
  font-size: 0.6em;
  font-weight: 600;
`;

const TableBody = styled.div`
  display: grid;
  grid-row-start: 2;
  grid-column-start: 2;
  grid-template-columns: repeat(6, 1fr);
  justify-items: stretch;
  align-items: stretch;
  grid-gap: 1px;
  background-color: ${props => props.theme.grey};
`;

class TableDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      days: ["TIME / DAY", "MON", "TUE", "WED", "THU", "FRI"],
      cells: [
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
        "6:00PM"
      ],
      schedule: [],
      colorCode: []
    };
    this.updateSchedule = this.updateSchedule.bind(this);
    this.updateColorCodes = this.updateColorCodes.bind(this);
  }

  componentDidMount = () => {
    var that = this;
    fetch("http://localhost:5000/get-schedule", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      }
    })
      .then(result => result.json())
      .then(schedule => {
        that.updateSchedule(schedule);
        console.log(schedule);
      });

    fetch("http://localhost:5000/get-course-colors", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      }
    })
      .then(result => result.json())
      .then(colorCodes => {
        that.updateColorCodes(colorCodes);
      });
  };

  updateColorCodes = cc => {
    let colorCode = [];
    cc.forEach(color => {
      let colorCodeItem = [color.course, color.color];
      colorCode.push(colorCodeItem);
    });
    this.setState({
      colorCode: colorCode
    });
    console.log(this.state.colorCode);
  };

  updateSchedule = cc => {
    let sortedByDay = [this.state.cells.slice(0, 19), [], [], [], [], []];
    cc.forEach(item => {
      sortedByDay[item.day].push(item);
    });
    this.setState({
      schedule: sortedByDay
    });
  };

  render() {
    return (
      <React.Fragment>
        <TableBody>
          {this.state.schedule.map((day, index) => (
            <div key={index}>
              <DayHeader className="cell">
                <p>{this.state.days[index]}</p>
              </DayHeader>
              <DayCol
                day={this.state.days}
                data={day}
                idx={index}
                times={this.state.cells}
                cc={this.state.colorCode}
              />
            </div>
          ))}
        </TableBody>
      </React.Fragment>
    );
  }
}

export default TableDisplay;
