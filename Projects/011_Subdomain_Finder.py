import requests

with open('011_Subdomains.txt', 'r') as subs:
    subdomains = subs.read().split('\n')

target = input('Escreva o domínio a analisar: ') or 'intuitivo.pt'
discovered_subdomains = []


def find_subdomains(domain, max_recursive_depth=1, show_tests=False, depth=0):
    if depth > max_recursive_depth:
        return
    global discovered_subdomains
    for sub in subdomains:
        url = f'http://{sub}.{domain}'
        try:
            if show_tests:
                print(f'Testando {url} ...')
            requests.get(url)
            sub_found = f'{sub}.{domain}'
            print(f'+ Discovered Subdomain: {url}')
            discovered_subdomains += [f'{sub_found}']
            find_subdomains(sub_found, max_recursive_depth, show_tests, depth + 1)
        except requests.ConnectionError:
            pass


print('\n')
find_subdomains(target, 1, True)

print(discovered_subdomains)
