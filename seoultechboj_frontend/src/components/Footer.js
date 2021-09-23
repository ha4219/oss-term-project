import React from 'react';
import styled, {css} from 'styled-components';


const Foot = styled.div`
  font-size: 0.75rem;
  padding: 2rem;
  background: rgb(111, 111, 111);
  color: white;
`;

const A = styled.a`
  text-decoration: none;
  color: white;
`;

const Footer = () => {
  return (
    <Foot>
      <div>powered by Dongha Jeong</div>
      <br/>
      <A href="https://github.com/ha4219/oss-term-project">project github</A>
    </Foot>
  );
};

export default Footer;