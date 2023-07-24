import React from 'react'
import BlogDetails from '@/components/BlogDetails'
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
      {/* <h1>Blog Title:{blog.title}</h1> */}
      <BlogDetails blog={blog} />
    </div>
  )
}


