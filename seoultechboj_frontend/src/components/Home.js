import React from 'react';
import LevelList from './level/LevelList';
import styled, {css} from 'styled-components';
import Introduction from './Introduction';


const Container = styled.div`
  background: rgb(233, 233, 233);
`;

const Body = styled.div`
  padding-top: 50px;
  padding-bottom: 50px;
  display: flex;
  width: 96%;
  max-width: 1100px;
  height: 100%;
  margin: 0 auto;
  align-items: center;
  justify-content: space-between;
`;

const Home = () => {
  return (
    <Container>
      <Introduction />
      <Body>
        <LevelList />
      </Body>
    </Container>
  );
};

export default Home;