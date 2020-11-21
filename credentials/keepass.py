from keepasshttp import keepasshttp


class KeePass:

    @staticmethod
    def get(url):
        print("Retrieve credentials for '" + url + "'")
        credentials = keepasshttp.get(url)
        if credentials is None:
            raise Exception(
                "KeePass entry for '" + url + "' not found!\nPlease add an entry with '" + url + "' as name or url")

        return credentials
