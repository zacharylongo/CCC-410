from intelxapi import intelx

# Initialize the IntelX class
intelx_instance = intelx('YOUR_API_KEY')  # Replace 'YOUR_API_KEY' with your actual API key

# Quick search example
results = intelx_instance.search('hackerone.com')
print(results)

# Advanced search example with maxresults override
results_advanced = intelx_instance.search('hackerone.com', maxresults=200)
print(results_advanced)

# Search in specific buckets example
buckets = ['darknet', 'leaks.public', 'leaks.private']
results_buckets = intelx_instance.search('hackerone.com', maxresults=200, buckets=buckets)
print(results_buckets)

# Filtering by date example
start_date = "2014-01-01 00:00:00"
end_date = "2014-02-02 23:59:59"
results_date_filter = intelx_instance.search('riseup.net', maxresults=200, datefrom=start_date, dateto=end_date)
print(results_date_filter)

# Filtering by media type example (Paste document)
media_type = 1  # Paste document
results_media_filter = intelx_instance.search('riseup.net', maxresults=200, media=media_type, datefrom=start_date, dateto=end_date)
print(results_media_filter)

# Statistics example
results_stats = intelx_instance.search('riseup.net', maxresults=1000)
stats = intelx_instance.stats(results_stats)
print(stats)

# Viewing file contents example
results_view = intelx_instance.search('riseup.net')
result_view = results_view['records'][0]
contents_view = intelx_instance.FILE_VIEW(result_view['type'], result_view['media'], result_view['storageid'], result_view['bucket'])
print(contents_view)

# Reading file example
results_read = intelx_instance.search('riseup.net')
result_read = results_read['records'][0]
intelx_instance.FILE_READ(result_read['systemid'], 0, result_read['bucket'], "file.txt")
