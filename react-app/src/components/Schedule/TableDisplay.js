import React, { Component } from "react";
import styled from "styled-components";
import Cell from "./Cell";

const Table = styled.div`
  display: grid;
  grid-template-columns: 6em 1fr;
  grid-template-rows: auto 1fr;
  justify-items: stretch;
  align-items: stretch;
  width: 100%;
  grid-gap: 1px;
`;

const Header = styled.div`
  display: grid;
  grid-column-start: 2;
  grid-template-columns: repeat(7, minmax(60px, 1fr));
  justify-items: stretch;
  align-items: stretch;
  grid-gap: 1px;
  background-color: ${props => props.theme.grey};

  .cell {
    font-size: 0.6em;
    background-color: white;
    text-align: center;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    border-top: 1px solid ${props => props.theme.grey};
    border-bottom: 1px solid ${props => props.theme.grey};
  }

  .cell:last-child {
    border-right: 1px solid ${props => props.theme.grey};
  }

  .cell:first-child {
    border-left: 1px solid ${props => props.theme.grey};
  }
`;

const TableSidebar = styled.div`
  display: grid;
  grid-row-start: 2;
  grid-column-start: 1;
  grid-template-rows: repeat(19, 1fr);
  justify-items: stretch;
  align-items: stretch;
  grid-gap: 1px;
  background-color: ${props => props.theme.grey};
  .cell {
    font-size: 0.6em;
    background-color: white;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    border-left: 1px solid ${props => props.theme.grey};
    border-right: 1px solid ${props => props.theme.grey};
  }
  .cell:first-child {
    border-top: 1px solid ${props => props.theme.grey};
  }
  .cell:last-child {
    border-bottom: 1px solid ${props => props.theme.grey};
  }
`;

const TableBody = styled.div`
  display: grid;
  grid-row-start: 2;
  grid-column-start: 2;
  grid-template-columns: repeat(7, 1fr);
  grid-template-rows: repeat(19, 1fr);
  justify-items: stretch;
  align-items: stretch;
  grid-gap: 1px;
  background-color: ${props => props.theme.grey};
`;

class TableDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      days: ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"],
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
        "5:30PM"
      ],
      schedule: []
    };
    this.updateSchedule = this.updateSchedule.bind(this);
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
  };

  updateSchedule = cc => {
    this.setState({
      schedule: cc
    });
  };

  render() {
    return (
      <React.Fragment>
        <Table>
          <Header className="header">
            {this.state.days.map(day => (
              <div className="cell" key={day}>
                <p>{day}</p>
              </div>
            ))}
          </Header>
          <TableSidebar>
            {this.state.cells.map(cell => (
              <div className="cell" key={cell}>
                <p>{cell}</p>
              </div>
            ))}
          </TableSidebar>
          <TableBody>
            {this.state.schedule.map((item, index) => (
              <Cell key={index} data={item} times={this.state.cells} />
            ))}
          </TableBody>
        </Table>
      </React.Fragment>
    );
  }
}

export default TableDisplay;
