import React from 'react'
import BlogComments from './BlogComments'
import { useSearchParams } from 'next/navigation';
import { BlogProps } from '@/types/types';

interface BlogDetailProps{
    blog:BlogProps
}

export default async function BlogDetails({blog}:BlogDetailProps) {
  return (
      <div className='pt-2 lg:pt-4 lg:pb-2 bg-white dark:bg-gray-900'>
          <div className="flex justify-between px-4 mx-auto max-w-screen-xl ">
              <article className='mx-auto w-full max-w-2xl format format-sm sm:format-base lg:format-lg format-blue dark:format-invert'>
                  <header className="mb-4 lg:mb-6 not-format">
                        <address className="flex items-center mb-6 not-italic">
                            <div className="inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white">
                                <img className="mr-4 w-16 h-16 rounded-full" src={blog.display_image} alt="Jese Leos" />
                                <div>
                                    <a href="#" rel="author" className="text-xl font-bold text-gray-900 dark:text-white">Jese Leos</a>
                                    <p className="text-base font-light text-gray-500 dark:text-gray-400">Graphic Designer, educator & CEO Flowbite</p>
                                    <p className="text-base font-light text-gray-500 dark:text-gray-400"><time dateTime="2022-02-08" title="February 8th, 2022">Feb. 8, 2022</time></p>
                                </div>
                            </div>
                        </address>
                      <h1 className="mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white">{blog.title}</h1>
                  </header>
                  <p className="lead">{blog.description}</p>
                <BlogComments comments={blog.comments} />
              </article>
              
          </div>
          
      </div>
  )
}
