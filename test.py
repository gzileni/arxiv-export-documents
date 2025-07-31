from arxiv_export import export_papers


def main():
    search_query = "quantum computing"
    download_path = "./arxiv_papers"
    max_results = 5

    papers = export_papers(
        search=search_query,
        path_download=download_path,
        max_results=max_results
    )

    for paper in papers:
        print(f"Title: {paper.title}")
        print(f"Authors: {', '.join(paper.authors)}")
        print(f"Summary: {paper.summary}")
        print(f"Link: {paper.link}")
        print(f"Path: {paper.path}")
        print(f"Documents: {len(paper.documents)}")
        print("-" * 80)


if __name__ == "__main__":
    main()
