from censys.search import CensysHosts, CensysCerts, SearchClient
from datetime import date
import os

#Get API ID and Secret
api_id = os.getenv('CENSYS_API_ID')
api_secret = os.getenv('CENSYS_API_SECRET')


# Initialize CensysHosts and CensysCerts
h = CensysHosts()
c = CensysCerts()

# Function to search hosts data set
def search_hosts(query, per_page=5, pages=1, fields=None, virtual_hosts=None):
    if fields:
        query = h.search(query, per_page=per_page, pages=pages, fields=fields)
    elif virtual_hosts:
        query = h.search(query, per_page=per_page, pages=pages, virtual_hosts=virtual_hosts)
    else:
        query = h.search(query, per_page=per_page, pages=pages)
    
    results = []
    for page in query:
        for host in page:
            results.append(host)
    return results

# Function to view specific host
def view_host(ip, at_time=None):
    if at_time:
        return h.view(ip, at_time=at_time)
    return h.view(ip)

# Function for bulk IP lookup
def bulk_view_hosts(ips):
    return h.bulk_view(ips)

# Function to aggregate hosts data set
def aggregate_hosts(query, field, num_buckets=5, virtual_hosts=None):
    if virtual_hosts:
        return c.v2.hosts.aggregate(query, field, num_buckets=num_buckets, virtual_hosts=virtual_hosts)
    return c.v2.hosts.aggregate(query, field, num_buckets=num_buckets)

# Function to fetch metadata about hosts
def get_hosts_metadata():
    return h.metadata()

# Function to view host names
def view_host_names(ip):
    return h.view_host_names(ip)

# Function to view host events
def view_host_events(ip, per_page=1, start_time=None, end_time=None):
    if start_time and end_time:
        return h.view_host_events(ip, per_page=per_page, start_time=start_time, end_time=end_time)
    return h.view_host_events(ip)

# Function to view host diff
def view_host_diff(ip, ip_b=None, at_time=None, at_time_b=None):
    if ip_b and at_time and at_time_b:
        return h.view_host_diff(ip=ip, ip_b=ip_b, at_time=at_time, at_time_b=at_time_b)
    elif ip_b:
        return h.view_host_diff(ip=ip, ip_b=ip_b)
    elif at_time and at_time_b:
        return h.view_host_diff(ip=ip, at_time=at_time, at_time_b=at_time_b)
    elif at_time:
        return h.view_host_diff(ip=ip, at_time=at_time)
    return h.view_host_diff(ip)

# Function to get hosts by certificate
def get_hosts_by_cert(cert_id):
    hosts, links = c.get_hosts_by_cert(cert_id)
    return hosts

# Function to get comments for a certificate
def get_comments(cert_id):
    return c.get_comments(cert_id)

# Example usage of the functions
if __name__ == "__main__":
    # Search hosts data set
    search_results = search_hosts("services.service_name: HTTP", per_page=5)
    print(search_results)

    # View specific host
    host_info = view_host("8.8.8.8")
    print(host_info)

    # Bulk IP lookup
    ips = ["1.1.1.1", "1.1.1.2", "1.1.1.3"]
    bulk_results = bulk_view_hosts(ips)
    print(bulk_results)

    # Aggregate hosts data set
    aggregate_report = aggregate_hosts("services.service_name: HTTP", "services.port", num_buckets=5)
    print(aggregate_report)

    # Fetch metadata about hosts
    metadata = get_hosts_metadata()
    print(metadata)

    # View host names
    host_names = view_host_names("1.1.1.1")
    print(host_names)

    # View host events
    host_events = view_host_events("1.1.1.1", per_page=1)
    print(host_events)

    # View host diff
    host_diff = view_host_diff("1.1.1.1", ip_b="1.1.1.2")
    print(host_diff)

    # Get hosts by certificate
    cert_id = "fb444eb8e68437bae06232b9f5091bccff62a768ca09e92eb5c9c2cf9d17c426"
    hosts_by_cert = get_hosts_by_cert(cert_id)
    print(hosts_by_cert)

    # Get comments for a certificate
    comments = get_comments(cert_id)
    print(comments)
