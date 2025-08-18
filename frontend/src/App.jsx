import React, { useState } from 'react'
import Signup from './Signup.jsx'
import Signin from './Signin.jsx'

export default function App() {
  const [tab, setTab] = useState('signup')
  return (
    <div style={{maxWidth: 460, margin: '40px auto', fontFamily: 'sans-serif'}}>
      <h2>Fullstack DevOps App</h2>
      <div style={{ display: 'flex', gap: 8 }}>
        <button onClick={() => setTab('signup')}>Signup</button>
        <button onClick={() => setTab('signin')}>Signin</button>
      </div>
      <div style={{marginTop: 16}}>
        {tab === 'signup' ? <Signup /> : <Signin />}
      </div>
    </div>
  )
}