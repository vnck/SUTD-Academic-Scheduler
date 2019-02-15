import React from "react";
import { shallow, mount } from "enzyme";
import Login from "../Login";

describe("Login", () => {
  test("should match snapshot", () => {
    const component = shallow(<Login />);
    expect(component).toMatchSnapshot();
  });

  test("on render should have empty state", () => {
    const component = mount(<Login />);
    const defaultProps = {
      user: "",
      password: ""
    };
    expect(component.state()).toEqual(defaultProps);
  });

  test("button disabled if empty state", () => {
    const component = mount(<Login />).find("button");
    const disabledState = component.props().disabled;
    expect(disabledState).toBeTruthy();
  });
});
