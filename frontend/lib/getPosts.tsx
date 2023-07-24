async function getPosts() {
    const res = await fetch('http://127.0.0.1:8000/api/posts/', { cache: "no-store" })
    
    if (!res.ok) {
      throw new Error('Failed to fetch data')
    }
   
    return res.json()
}