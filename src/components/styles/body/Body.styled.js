import styled from "styled-components";


export const Body = styled.section`
    width: 100%;
    height: 50vh;
    color: black;
    /* background-color: #282c34; // 오묘한 예쁜 컬러 */
    background-color: white;
    position: relative; // 다른 엘리먼트들과 겹치지 않도록
    display: flex; 
    justify-content: 'center'; // display를 flex로 해주었기 때문에 justify-content center 가능
    padding: 10px 0 0 30px;
    /* &::before {
        content: '';
        position: absolute;
        width: 100%; 
        height: 100%;
        top: 0;
        left: 0;
        display: inline-block;
        border-radius: 0 0 50% 50% / 0 0 100% 100%;
        transform: scaleX(1.5);
        background-position: right top;
        background-size: 100vw 200px;
        background-color: white;
    } */
`

export const MainBody = styled.div`
    position: relative;
`

