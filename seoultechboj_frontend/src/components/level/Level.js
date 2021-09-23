import React from 'react';
import styled, {css} from 'styled-components';
import {Link} from 'react-router-dom';


const Container = styled.tr`
  width: "100%";
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

const Item3 = styled.td`
  padding: 0.5rem 0.75rem;
  text-align: left;
`;

const Img = styled.img`
  width: 1.2em;
  height: 1.2em;
  line-height: inherit;
  vertical-align: middle;
`

const Unrated = styled.span`
  color: rgb(0, 0, 0);
`;

const Bronze = styled.span`
  color: rgb(173, 86, 0);
`;

const Silver = styled.span`
  color: rgb(67, 95, 122);
`;

const Gold = styled.span`
  color: rgb(236, 154, 0);
`;

const Platinum = styled.span`
  color: rgb(39, 226, 164);
`;

const Diamond = styled.span`
  color: rgb(0, 180, 252);
`;

const Ruby = styled.span`
  color: rgb(255, 0, 98);
`;

const Progress = styled.progress`
  color: rgb(255, 0, 98);
  width: parent;
`;

const Level = ({props, idx}) => {
  const getLevel = (level) => {
    switch (Number(level)) {
      case 0:
        return <Unrated> Unrated</Unrated>;
      case 1:
        return <Bronze> Bronze V</Bronze>
      case 2:
        return <Bronze> Bronze IV</Bronze>
      case 3:
        return <Bronze> Bronze III</Bronze>
      case 4:
        return <Bronze> Bronze II</Bronze>
      case 5:
        return <Bronze> Bronze I</Bronze>
      case 6:
        return <Silver> Silver V</Silver>
      case 7:
        return <Silver> Silver IV</Silver>
      case 8:
        return <Silver> Silver III</Silver>
      case 9:
        return <Silver> Silver II</Silver>
      case 10:
        return <Silver> Silver I</Silver>
      case 11:
        return <Gold> Gold V</Gold>
      case 12:
        return <Gold> Gold IV</Gold>
      case 13:
        return <Gold> Gold III</Gold>
      case 14:
        return <Gold> Gold II</Gold>
      case 15:
        return <Gold> Gold I</Gold>
      case 16:
        return <Platinum> Platinum V</Platinum>
      case 17:
        return <Platinum> Platinum IV</Platinum>
      case 18:
        return <Platinum> Platinum III</Platinum>
      case 19:
        return <Platinum> Platinum II</Platinum>
      case 20:
        return <Platinum> Platinum I</Platinum>
      case 21:
        return <Diamond> Diamond V</Diamond>
      case 22:
        return <Diamond> Diamond IV</Diamond>
      case 23:
        return <Diamond> Diamond III</Diamond>
      case 24:
        return <Diamond> Diamond II</Diamond>
      case 25:
        return <Diamond> Diamond I</Diamond>
      case 26:
        return <Ruby> Ruby V</Ruby>
      case 27:
        return <Ruby> Ruby IV</Ruby>
      case 28:
        return <Ruby> Ruby III</Ruby>
      case 29:
        return <Ruby> Ruby II</Ruby>
      case 30:
        return <Ruby> Ruby I</Ruby>
      default:
        return "INF";
    }
  }
  return (
    <Container idx={Number(idx)}>
      <Item1>
        <Link to={`/problem/${Number(props.level)}`}>
          <Img src={`/static/${props.level}.svg`}/>
          {getLevel(props.level)}
        </Link>
      </Item1>
      <Item1>
        {/* <NotA1 href={`https://boj.kr/${props.problemId}`}>
          {props.problemId}
        </NotA1> */}
        {props.notSolved}
      </Item1>
      <Item1>
        {props.solved}
        {/* <NotA2 href={`https://boj.kr/${props.problemId}`}>
          {props.titleKo}
        </NotA2> */}
      </Item1>
      <Item2>{props.total}</Item2>
      <Item3>
        <Progress max={props.total} value={props.solved}/>
      </Item3>
    </Container>
  );
};

export default Level;