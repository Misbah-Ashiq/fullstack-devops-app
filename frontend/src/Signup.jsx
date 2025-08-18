import React, { useState } from 'react'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:5000'

export default function Signup() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [msg, setMsg] = useState('')

  const submit = async (e) => {
    e.preventDefault()
    setMsg('')
    try {
      const res = await fetch(`${API_BASE}/api/signup`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ email, password })
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.error || 'Signup failed')
      setMsg('Signup successful ✔')
    } catch (err) {
      setMsg(err.message)
    }
  }

  return (
    <form onSubmit={submit}>
      <div><input placeholder="email" value={email} onChange={e=>setEmail(e.target.value)} /></div>
      <div><input type="password" placeholder="password" value={password} onChange={e=>setPassword(e.target.value)} /></div>
      <button type="submit">Create account</button>
      {msg && <p>{msg}</p>}
    </form>
  )
}