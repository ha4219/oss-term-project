import React from 'react';
import styled, {css} from 'styled-components';


const Container = styled.div`
  text-align: center;
  justify-content:center;
`;

const Description = styled.div`
  padding: 50px 0px 50px 0px;
  text-align: center;
  font-weight: 400;
`;

const Todo = styled.div`
  padding-left: 30%;
  text-align: left;
  font-weight: bold;
  line-height: 1.6;
`;

const Introduction = () => {
  return (
    <Container>
      <Description>
        안녕하세요. 서울과학기술대학교 컴퓨터공학과 재학중인 정동하입니다.<br/>
        사이트 목적은 백준 온라인 저지 사이트에서 학교 순위를 높이고자 서울과학기술대학교 학생들이 안 푼 문제를 찾아주는 서비스입니다.<br/>
        개발기간: 이번 추석 때
        <br/>
        <br/>
        Backend : Django<br/>
        Frontend : React<br/>
        <br/>
        <Todo>
        TODO : <br/>
          - 실시간 학교 랭킹<br/>
          - not solved 문제 푼 user 실시간 업데이트<br/>
          - sqlite -> mysql -> graphql<br/>
          - 문제 추천
        </Todo>
      </Description>
    </Container>
  );
};

export default Introduction;