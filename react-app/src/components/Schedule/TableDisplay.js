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

const FilterContainer = styled.div`
  display: flex;
  width: 80%;
  justify-content: center;
  padding: 0.6rem;
`;

const FilterContainerChild = styled.div`
  padding: 0 3rem;
  display: flex;
  p {
    margin-right: 0.4rem;
  }
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
      colorCode: [],
      profs: [],
      courses: [],
      studentGroups: [],
      profFilter: "",
      coursesFilter: "",
      studentGroupsFilter: ""
    };

    this.updateSchedule = this.updateSchedule.bind(this);
    this.updateColorCodes = this.updateColorCodes.bind(this);
    this.updateFilters = this.updateFilters.bind(this);
    this.updateTable = this.updateTable.bind(this);
  }

  componentDidMount = () => {
    this.updateTable();
  };

  updateTable = () => {
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
        let filtered_schedule;
        if (this.props.isCoordinator) {
          filtered_schedule = schedule;
        } else {
          filtered_schedule = schedule.filter(
            items => items.professors === this.props.name
          );
        }
        that.updateSchedule(filtered_schedule);
        that.updateFilters(filtered_schedule);
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

  updateFilters = cc => {
    let profs = [];
    let courses = [];
    let studentGroups = [];
    cc.forEach(cc => {
      if (cc.professors.includes(",")) {
        let profls = cc.professors.split(",");
        profls.forEach(prof => {
          if (!profs.includes(prof)) {
            profs.push(prof);
          }
        });
      } else {
        if (!profs.includes(cc.professors)) {
          profs.push(cc.professors);
        }
      }
      if (cc.studentGroups.includes(",")) {
        let sGls = cc.studentGroups.split(",");
        sGls.forEach(sg => {
          if (!sGls.includes(sg)) {
            sGls.push(sg);
          }
        });
      } else {
        if (!studentGroups.includes(cc.studentGroups)) {
          studentGroups.push(cc.studentGroups);
        }
      }
      if (!courses.includes(cc.course)) {
        courses.push(cc.course);
      }
    });
    this.setState({
      profs: profs,
      courses: courses,
      studentGroups: studentGroups
    });
  };

  setFilter = event => {
    let opt = event.target.value;
    if (opt === "") {
      this.setState({
        profFilter: "",
        coursesFilter: "",
        studentGroupsFilter: ""
      });
    } else if (this.state.profs.includes(opt)) {
      this.setState({
        profFilter: opt,
        coursesFilter: "",
        studentGroupsFilter: ""
      });
    } else if (this.state.courses.includes(opt)) {
      this.setState({
        profFilter: "",
        coursesFilter: opt,
        studentGroupsFilter: ""
      });
    } else if (this.state.studentGroups.includes(opt)) {
      this.setState({
        profFilter: "",
        coursesFilter: "",
        studentGroupsFilter: opt
      });
    }
  };

  render() {
    let ProfFilter;
    if (this.props.isCoordinator) {
      ProfFilter = (
        <FilterContainerChild>
          <p>Professors: </p>
          <select onChange={this.setFilter} value={this.state.profFilter}>
            <option />
            {this.state.profs.map((prof, index) => (
              <option key={index}>{prof}</option>
            ))}
          </select>
        </FilterContainerChild>
      );
    }
    return (
      <React.Fragment>
        <FilterContainer>
          {ProfFilter}
          <FilterContainerChild>
            <p>Courses: </p>
            <select onChange={this.setFilter} value={this.state.coursesFilter}>
              <option />
              {this.state.courses.map((course, index) => (
                <option key={index}>{course}</option>
              ))}
            </select>
          </FilterContainerChild>
          <FilterContainerChild>
            <p>Student Group: </p>
            <select
              onChange={this.setFilter}
              value={this.state.studentGroupsFilter}
            >
              <option />
              {this.state.studentGroups.map((sg, index) => (
                <option key={index}>{sg}</option>
              ))}
            </select>
          </FilterContainerChild>
        </FilterContainer>
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
                filter={[
                  this.state.profFilter,
                  this.state.coursesFilter,
                  this.state.studentGroupsFilter
                ]}
              />
            </div>
          ))}
        </TableBody>
      </React.Fragment>
    );
  }
}

export default TableDisplay;
