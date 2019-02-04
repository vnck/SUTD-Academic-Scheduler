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
  grid-template-columns: repeat(7, 1fr);
  justify-items: stretch;
  align-items: stretch;
  grid-gap: 1px;
  background-color: ${props => props.theme.grey};
  .cell {
    font-size: 0.8em;
    padding: 0.2em 1em;
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
  .cell: first-child {
    border-left: 1px solid ${props => props.theme.grey};
  }
`;

const TableSidebar = styled.div`
  display: grid;
  grid-row-start: 2;
  grid-column-start: 1;
  grid-template-rows: repeat(22, 1fr);
  justify-items: stretch;
  align-items: stretch;
  grid-gap: 1px;
  background-color: ${props => props.theme.grey};
  .cell {
    font-size: 0.8em;
    padding: 0.2em 1em;
    background-color: white;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    border-left: 1px solid ${props => props.theme.grey};
    border-right: 1px solid ${props => props.theme.grey};
  }
  .cell: first-child {
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
  justify-items: stretch;
  align-items: stretch;
  grid-gap: 1px;
  background-color: ${props => props.theme.grey};
`;

const DayCol = styled.div`
  display: grid;
  grid-template-rows: repeat(22, 1fr);
  justify-items: stretch;
  align-items: stretch;
  grid-gap: 1px;
  background-color: ${props => props.theme.silver};
  .cell {
    padding: 0.4em 1em;
    background-color: white;
  }
  .empty {
    padding: 0.4em 1em;
    background-color: white;
  }
`;

class TableDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      days: ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"],
      cells: [
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
      activities: [
        [
          {
            name: "Digital World",
            timing: "8AM - 9AM",
            venue: "2.505 LT2",
            instructor: "John. O",
            code: "50.003",
            color: "#bba",
            start: 1,
            end: 4
          },
          { start: 4, end: 5 },
          {
            name: "Digital World",
            timing: "8AM - 9AM",
            venue: "2.505 LT2",
            instructor: "John. O",
            code: "50.002",
            color: "#bba",
            start: 8,
            end: 10
          },
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          ""
        ],
        [
          { start: 4, end: 5 },
          {
            name: "Digital World",
            timing: "8AM - 9AM",
            venue: "2.505 LT2",
            instructor: "John. O",
            code: "50.013",
            color: "#bba",
            start: 10,
            end: 14
          },
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          ""
        ],
        [
          { start: 4, end: 5 },
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          ""
        ],
        [],
        [],
        [],
        []
      ]
    };
  }

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
            {this.state.activities.map((day, index) => (
              <DayCol key={day + index}>
                {day.map(
                  (activity, index) =>
                    activity !== "" && <Cell key={index} data={activity} />
                )}
              </DayCol>
            ))}
          </TableBody>
        </Table>
      </React.Fragment>
    );
  }
}

export default TableDisplay;
