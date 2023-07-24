import React from 'react'
import Image from 'next/image'
// import { posts } from '@/constants/blogs'

async function getPosts() {
  const res = await fetch('http://127.0.0.1:8000/api/posts/', { cache: "no-store" })
  
  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }
 
  return res.json()
}

export default async function BlogSection() {
  const posts = await getPosts();

  return (
    <div className="bg-white py-24 sm:py-32">
    <div className="mx-auto max-w-7xl px-6 lg:px-8">
      <div className="mx-auto max-w-2xl lg:mx-0">
        <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">From the blog</h2>
        <p className="mt-2 text-lg leading-8 text-gray-600">
          Learn how to grow your business with our expert advice.
        </p>
      </div>
      <div className="mx-auto mt-10 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-8 border-t border-gray-200 pt-10 sm:mt-16 sm:pt-16 lg:mx-0 lg:max-w-none lg:grid-cols-3">
        {posts.map((post) => (
          <article key={post.slug} className="flex max-w-xl flex-col items-start justify-between">
            <div>
                <Image 
                    src={post.display_image} 
                    alt={post.title} 
                    height={200} 
                    width={300}
                    className='w-full rounded mb-2'
                    // fill 
                />
            </div>
            <div className="flex items-center gap-x-4 text-xs">
              <time dateTime={post.published_at} className="text-gray-500">
                {post.published_at}
              </time>
              <a
                href='#'
                className="relative z-10 rounded-full bg-gray-50 px-3 py-1.5 font-medium text-gray-600 hover:bg-gray-100"
              >
                {/* {post.category.title} */}
                {post.slug}
              </a>
            </div>
            <div className="group relative">
              <h3 className="mt-3 text-lg font-semibold leading-6 text-gray-900 group-hover:text-gray-600">
                <a href={`/blog/${post.slug}`}>
                  <span className="absolute inset-0" />
                  {post.title}
                </a>
              </h3>
              <p className="mt-1 line-clamp-3 text-sm leading-6 text-gray-600">{post.description.substring(0, 100)}...</p>
            </div>
            <div className="relative mt-3 flex items-center gap-x-4">
              <img src={post.image_url} alt="" className="h-10 w-10 rounded-full bg-gray-50" />
              <div className="text-sm leading-6">
                <p className="font-semibold text-gray-900">
                  <a href='#'>
                    <span className="absolute inset-0" />
                    {post.title}
                  </a>
                </p>
                <p className="text-gray-600">
                  {/* {post.author.role} */}
                  Branch Manager
                </p>
              </div>
            </div>
          </article>
        ))}
      </div>
    </div>
  </div>
  )
}
