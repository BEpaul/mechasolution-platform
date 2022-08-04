import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

function LoginPage() {

  const navigate = useNavigate();

  const [Email, setEmail] = useState("")
  const [Password, setPassword] = useState("")

  const onEmailHandler = (event) => {
    setEmail(event.currentTarget.value)
  }

  const onPasswordHandler = (event) => {
    setPassword(event.currentTarget.value)
  }

  const onSubmitHandler = (event) => {
    event.preventDefault();

    // 회원정보가 맞는지 아닌지 확인

    // 로그인 성공 -> 랜딩페이지로 이동
    navigate('/');

  }

  return (
          <div
            style={{
              display: 'flex', justifyContent: 'center', alignItems: 'center', width: '100%', height: '100vh'
            }}>
            <form style={{ display: 'flex', flexDirection: 'column' }}
              onSubmit={onSubmitHandler}
            >
              <label>Email</label>
              <input type="email" value={Email} onChange={onEmailHandler} />

              <label>Password</label>
              <input type="password" value={Password} onChange={onPasswordHandler} />


              <br />
              <button type="submit">
                Login
              </button>

            </form>
          </div>
  )
}

export default LoginPage