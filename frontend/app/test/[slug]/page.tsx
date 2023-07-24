import React from 'react'
import getPostDetail from '@/lib/getPostDetail'

type Params = {
  params: {
    slug:string
  }
}
type Blog = {
  title:string
}
export default async function Page({ params: { slug } }: Params) {
  const blogData: Promise<Blog> = getPostDetail(slug)
  const [blog] = await Promise.all([blogData])
  return (
      <div>
      <h1>Slug:{slug}</h1>
      <h2>Title: {blog.title}</h2>
      </div>
  )
}
