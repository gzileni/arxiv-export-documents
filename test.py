import asyncio
from arxiv_export_documents import export_papers


async def main():
    search_query = "quantum computing"
    download_path = "./arxiv_papers"
    max_results = 5

    async for paper in export_papers(
        search=search_query,
        path_download=download_path,
        max_results=max_results
    ):
        print(f"Downloaded paper: {paper.title}")
        print(f"Authors: {', '.join(paper.authors)}")
        print(f"Summary: {paper.summary}")
        print(f"Link: {paper.link}")
        print(f"Path: {paper.path}")
        print(f"Documents: {len(paper.documents)}")
        print("-" * 80)


if __name__ == "__main__":
    asyncio.run(main())
