from intelxapi import intelx

def perform_quick_search(api_key, search_term):
    intelx_instance = intelx(api_key)
    results = intelx_instance.search(search_term)
    return results

def perform_advanced_search(api_key, search_term, max_results=100, buckets=None, date_from=None, date_to=None, media_type=0):
    intelx_instance = intelx(api_key)
    results = intelx_instance.search(
        search_term,
        maxresults=max_results,
        buckets=buckets,
        datefrom=date_from,
        dateto=date_to,
        media=media_type
    )
    return results

def perform_statistics(api_key, search_results):
    intelx_instance = intelx(api_key)
    stats = intelx_instance.stats(search_results)
    return stats

def view_file_contents(api_key, search_results, index=0):
    intelx_instance = intelx(api_key)
    result = search_results['records'][index]
    contents = intelx_instance.FILE_VIEW(result['type'], result['media'], result['storageid'], result['bucket'])
    return contents

def read_file(api_key, search_results, index=0, file_name="file.txt"):
    intelx_instance = intelx(api_key)
    result = search_results['records'][index]
    intelx_instance.FILE_READ(result['systemid'], 0, result['bucket'], file_name)

def get_media_options():
    media_options = {
        0: 'All',
        1: 'Paste document',
        2: 'Paste user',
        3: 'Forum',
        4: 'Forum board',
        5: 'Forum thread',
        6: 'Forum post',
        7: 'Forum user',
        8: 'Screenshot of website',
        9: 'HTML copy of website',
        13: 'Tweet',
        14: 'URL',
        15: 'PDF document',
        16: 'Word document',
        17: 'Excel document',
        18: 'Powerpoint document',
        19: 'Picture',
        20: 'Audio file',
        21: 'Video file',
        22: 'Container file (ZIP/RAR/TAR, etc)',
        23: 'HTML file',
        24: 'Text file'
    }
    return media_options

def main():
    api_key = input("Enter your IntelX API key: ")
    search_term = input("Enter the domain or search term: ")

    # Ask the user if they want to perform an advanced search
    perform_advanced_search = input("Do you want to perform an advanced search? (Yes/No): ").lower() == 'yes'

    if perform_advanced_search:
        # Fields for advanced search
        max_results = int(input("Enter the maximum number of results (default is 100): ") or 100)
        buckets = input("Enter the buckets (comma-separated, e.g., darknet,leaks.public): ").split(',')
        date_from = input("Enter the start date (format: YYYY-MM-DD HH:mm:ss): ")
        date_to = input("Enter the end date (format: YYYY-MM-DD HH:mm:ss): ")

        # Prompt user to specify media types
        specify_media_types = input("Would you like to specify media types? (Yes/No): ").lower() == 'yes'

        if specify_media_types:
            # Get media options
            media_options = get_media_options()

            # Display media options
            print("\nMedia Types:")
            for code, media_type in media_options.items():
                print(f"{code}: {media_type}")

            # Prompt user to enter media types
            media_type = int(input("Enter the media type code (e.g., 1 for Paste document): "))
        else:
            media_type = 0  # Default to all media types

        # Advanced search example
        advanced_search_results = perform_advanced_search(api_key, search_term, max_results, buckets, date_from, date_to, media_type)
        print("\nAdvanced Search Results:")
        print(advanced_search_results)

    else:
        # Quick search example
        quick_search_results = perform_quick_search(api_key, search_term)
        print("Quick Search Results:")
        print(quick_search_results)

    # Statistics example
    stats = perform_statistics(api_key, advanced_search_results if perform_advanced_search else quick_search_results)
    print("\nStatistics:")
    print(stats)

    # View file contents example
    contents = view_file_contents(api_key, advanced_search_results) if perform_advanced_search else view_file_contents(api_key, quick_search_results)
    print("\nFile Contents:")
    print(contents)

    # Read file example
    read_file(api_key, advanced_search_results) if perform_advanced_search else read_file(api_key, quick_search_results)
    print("\nFile 'file.txt' saved successfully.")

if __name__ == "__main__":
    main()
