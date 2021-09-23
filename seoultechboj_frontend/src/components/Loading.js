import React from 'react';
import styled, {css} from 'styled-components';


const Load = styled.div`
  text-align: center;
  vertical-align: middle;
  justify-content: center;
`;

const Img = styled.img`
  width: 5em;
  height: 5em;
  line-height: inherit;
  vertical-align: middle;
`

const Loading = () => {
  return (
    <Load>
      <Img src={`/static/Loading.gif`} />           
    </Load>
  );
};

export default Loading;