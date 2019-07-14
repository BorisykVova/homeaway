import typing as typ

OWNER = '''ownersListingProfile { 
            aboutYou 
            whyHere 
            storyPhoto 
            yearPurchased 
            uniqueBenefits 
        }
        contact { 
            name 
            languagesSpoken 
            ownerProfilePhoto 
            memberSince 
            redirectUrl 
            hasPhoneNumber
            phones { 
                phoneNumber 
                notes 
                areaCode 
                extension 
                phoneType 
                telScheme 
                countryCode 
                phoneNumber 
            }
        }'''

IMAGES = 'images { uri height width }'

PRICE = 'priceSummary{ pricePeriodDescription type amount currency formattedAmount }'


def build_post_json(listing_id: str, query_type=typ.Dict[str, bool]) -> dict:
    args = {'owner':  OWNER if query_type['owner'] else '',
            'images': IMAGES if query_type['images'] else '',
            'price': PRICE if query_type['price'] else ''}
    return {
        "operationName": "ownerOfListing",
        "variables": {
            "listingId": listing_id,
        },
        "query": 'query ownerOfListing($listingId: String!) { listing(listingId: $listingId) {' +
                 '{owner}{images}{price}'.format(**args) + '} }'}
