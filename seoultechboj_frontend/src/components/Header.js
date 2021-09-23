import React from 'react';
import styled, {css} from 'styled-components';


const Head = styled.div`
  position: sticky;
  left: 0;
  top: 0;
  width: 100%;
  height: 50px;
  z-index: 9;
  background: white;
  text-align: center;
  background: rgb(111,111,111);
  color: white;
`;

const Span = styled.span`
  font-size: 2rem;
  font-weight: bold;
  text-align: center;
`

const Header = () => {
  return (
    <Head>
      <Span>SeoulTech Boj Group</Span>
    </Head>
  );
};

export default Header;