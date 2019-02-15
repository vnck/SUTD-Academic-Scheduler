import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`

  body {
    font-family: Helvetica, sans-serif;
    background-color: ${props => props.theme.white};
    width: 100%;
    height: 100%;
  }

  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }
`;
