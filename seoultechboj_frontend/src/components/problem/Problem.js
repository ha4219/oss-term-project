import React from 'react';
import styled, {css} from 'styled-components';


const Container = styled.tr`
  background: ${props => props.idx&1? ('rgb(247, 248, 249)'): ('rgb(255, 255, 255)')};
  font-weight: 400;
  line-height: 1.3;
`;

const NotA1= styled.a`
  text-decoration: none;
  color: black;
  font-weight:bold;
`;

const NotA2 = styled.a`
  text-decoration: none;
  color: black;
`;

const Item1 = styled.td`
  padding: 0.5rem 0.75rem;
  text-align: left;
`;
const Item2 = styled.td`
  padding: 0.5rem 0.75rem;
  text-align: right;
`;

const Img = styled.img`
  width: 1.2em;
  height: 1.2em;
  line-height: inherit;
  vertical-align: middle;
`

const Problem = ({props, idx}) => {
  return (
    <Container idx={Number(idx)}>
      <Item1>
        <NotA1 href={`https://boj.kr/${props.problemId}`}>
          <Img src={`/static/${props.level}.svg`}/>           
          {props.problemId}
        </NotA1>
      </Item1>
      <Item1>
        <NotA2 href={`https://boj.kr/${props.problemId}`}>
          {props.titleKo}
        </NotA2>
      </Item1>
      <Item2>{props.acceptedUserCount}</Item2>
      <Item2>{Number(props.averageTries).toFixed(2)}</Item2>
    </Container>
  );
};

export default Problem;