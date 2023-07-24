import React from 'react'

export default async function getPostDetail(slug:string) {
  const res = await fetch(`http://127.0.0.1:8000/api/posts/${slug}/`, { cache: "no-store" })

  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }
  return res.json()
}
