import React, {useReducer, useEffect} from 'react';
import axios from 'axios';
import Level from './Level';
import Loading from '../Loading';
import styled, {css} from 'styled-components';



const reducer = (state, action) => {
  switch (action.type) {
    case 'LOADING':
      return {
        loading: true,
        data: null,
        error: null,
      };
    case 'SUCCESS':
      return {
        loading: false,
        data: action.data,
        error: null,
      };
    case 'ERROR':
      return {
        loading: false,
        data: null,
        error: action.error,
      };
    default:
      throw new Error(`Unhandled action type: ${action.type}`);
  }
}

const Container = styled.table`
  width: 100%;
  margin: 0px;
  border-spacing: 0px;
`;

const Thead = styled.tr`
  background: black;
  color: white;
  font-weight: bold;
  text-align: center;
  line-height: 1.6;
  width: 100%;
  margin:0px;
`;

const Td = styled.td`

`;

const LevelList = () => {
  const [state, dispatch] = useReducer(reducer, {
    loading: false,
    data: null,
    error: null,
  });

  const fetchLevel = async() => {
    dispatch({type: 'LOADING'});
    try{
      const response = await axios.get(
        "/api/v2/level/"
      );
      dispatch({type:'SUCCESS', data: response.data });
    } catch(e) {
      dispatch({type:'ERROR', error: e});
    }
  };

  useEffect(() => {
    fetchLevel();
  }, []);

  const {loading, data, error} = state;

  if (loading) return <Loading/>;
  if (error) return <div>error</div>;
  if (!data) return <div>data is null</div>;
  return (
    <Container>
      <Thead>
        <Td>레벨</Td>
        <Td>미해결</Td>
        <Td>해결</Td>
        <Td>전체</Td>
        <Td>진행도</Td>
      </Thead>
      {data.map((dat, idx) => (
        <Level idx={idx} props={dat}/>
      ))}
    </Container>
  );
};

export default LevelList;