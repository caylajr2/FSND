
import pytest
import requests

# Public Information
BASE_URL = "https://render-deployment-example-32e1.onrender.com/"  # Replace with your actual host

# Customer 1 Information
CUSTOMER1_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InFVUTREUnZUeUZGWU80QllkTGtpMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hYXZoM3JiYWduNjFobnYzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2N2RhMWQzNmQzNTAxYmRlMDIxY2ZjNjkiLCJhdWQiOiJzaG9wcGUiLCJpYXQiOjE3NDI4NTI4NzksImV4cCI6MTc0MjkzOTI3OSwic2NvcGUiOiIiLCJhenAiOiJ0WDV5SXQ3SlZoRGQyU2hoQkFjRnhYanJrTmRvN2tIdyIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjdXN0b21lciIsImVkaXQ6Y3VzdG9tZXIiLCJnZXQ6Y3VzdG9tZXIiLCJnZXQ6aXRlbSIsImdldDppdGVtcyIsInBsYWNlOm9yZGVyIiwicG9zdDpjdXN0b21lciIsInJlc2VydmU6aXRlbSJdfQ.D_AY92Kfm05PxIEUrBE5yDiU6Gb9Wvtx7nhdSaJavsO5foz7K0CGDdqxRhR188nY8Ct-l1KkUpH_IeA0O28L8F9AX0QVLJxyW12CaeNTdaL-l6AdzsmTkI0atpgUjbfTxZZ9hiuLMVce3rW5iJpUQbeXcNArgtjY0u5pMbQZhXFJSMRerxrrQxpkTXN2kzP27kkV4sQkKVjudPH14APHV6hWgzG5e_TewRuvRkP9tnTIbPLkJx5wk6Qdt5duf307XElob0vcJIHVluaOokn1gE62iLaBm6XP-gLj5vtWf-iInMOP6psv4Rs0G42LO8pRlzeVypOdpZKk1z8KJLbajA"
CUSTOMER1_HEADERS = {"Authorization": f"Bearer {CUSTOMER1_TOKEN}"}


# Customer 2 Information
CUSTOMER2_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InFVUTREUnZUeUZGWU80QllkTGtpMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hYXZoM3JiYWduNjFobnYzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2N2RhMWRhZDc1ODY4YmUzNmNmYmUyMzEiLCJhdWQiOiJzaG9wcGUiLCJpYXQiOjE3NDI4NTMxODQsImV4cCI6MTc0MjkzOTU4NCwic2NvcGUiOiIiLCJhenAiOiJ0WDV5SXQ3SlZoRGQyU2hoQkFjRnhYanJrTmRvN2tIdyIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjdXN0b21lciIsImVkaXQ6Y3VzdG9tZXIiLCJnZXQ6Y3VzdG9tZXIiLCJnZXQ6aXRlbSIsImdldDppdGVtcyIsInBsYWNlOm9yZGVyIiwicG9zdDpjdXN0b21lciIsInJlc2VydmU6aXRlbSJdfQ.UiU2Sqeh8-RZ2H7RhetDWQkyNtikh1Tg6OWURIy46CJNJNRFEI28UOpiZG244HAs4jl0tezPeJAMJV8FWm8w_STXpI_U61rpy9qZyymucUgruKgH1iIwAOsmkF71aPM1HddH7lPxBoHq2Ru7wBFbDxEOCjoePFP3KPZQaHqJibxg_uJQF58y8Wff4oiqSPQBfUj90jXxjisb4vHJRnNsypszspym4rKqetSVwGFQ-W9KBz5qgtJ0aC4ZXhnzs-49G2hBt_45TzRHTfQnq4Lx6Jozhg5eeesmlC1kDaBu49Hp_CglmR6Zs_T0Vkruf90UE7qM0qECm3yTe6bpP9hJfQ"
CUSTOMER2_HEADERS = {"Authorization": f"Bearer {CUSTOMER2_TOKEN}"}


# Customer 3 Information
CUSTOMER3_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InFVUTREUnZUeUZGWU80QllkTGtpMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hYXZoM3JiYWduNjFobnYzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2N2RhMjg0MTkxYjI3NWZkNDBlNGE1YjAiLCJhdWQiOiJzaG9wcGUiLCJpYXQiOjE3NDI4NTMyMTMsImV4cCI6MTc0MjkzOTYxMywic2NvcGUiOiIiLCJhenAiOiJ0WDV5SXQ3SlZoRGQyU2hoQkFjRnhYanJrTmRvN2tIdyIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjdXN0b21lciIsImVkaXQ6Y3VzdG9tZXIiLCJnZXQ6Y3VzdG9tZXIiLCJnZXQ6aXRlbSIsImdldDppdGVtcyIsInBsYWNlOm9yZGVyIiwicG9zdDpjdXN0b21lciIsInJlc2VydmU6aXRlbSJdfQ.yk9RLiXg5BiL02nxosnb2bSpyjp9eUIpP0BNEIifUYh5jh-rndXShTvgvmM5BZjSv5-u5UHcgzX7JS_fyUGuivOzbc-TW4FDl4y86fJLHgxDcom1GEoSLFB0EuW7Ch-Ad4CJI3MdqzOtoZo9WiCBpHXFUez20Typq0jr4_WEAChJAIZyK1_KYzsbWzLwwCAUClpwBOMHlhEBFAUktvPuzzoKwJBnQI4D-NwtVbtcSSJB0mWgfqO3llWlaUeNzlvE-pmwLLRBI4l6zc8xHAaLEXBFZ45pJ5IPiZVsOQ2QNxkNjqu92yc7IbS5E-svjXSDBp-den9VUSF1FAGqv8wkvQ"
CUSTOMER3_HEADERS = {"Authorization": f"Bearer {CUSTOMER3_TOKEN}"}



# Owner Information
OWNER_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InFVUTREUnZUeUZGWU80QllkTGtpMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hYXZoM3JiYWduNjFobnYzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2N2RhMWMzYzY0ZjJiYTgyNzg4YTNiMDIiLCJhdWQiOiJzaG9wcGUiLCJpYXQiOjE3NDI4NTMxMzIsImV4cCI6MTc0MjkzOTUzMiwic2NvcGUiOiIiLCJhenAiOiJ0WDV5SXQ3SlZoRGQyU2hoQkFjRnhYanJrTmRvN2tIdyIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjdXN0b21lciIsImRlbGV0ZTppdGVtIiwiZWRpdDpjdXN0b21lciIsImVkaXQ6aXRlbSIsImdldDpjdXN0b21lciIsImdldDpjdXN0b21lcnMiLCJnZXQ6aXRlbSIsImdldDppdGVtcyIsInBsYWNlOm9yZGVyIiwicG9zdDpjdXN0b21lciIsInBvc3Q6aXRlbSIsInJlc2VydmU6aXRlbSJdfQ.BMUY6gRvJiBEbO8-a2tR1X6fEZDW3dFMevQ1D31ts0jTzcV_u_e0IU--Lb3e7unyIH9ANKXXbO0FkGz6Tp7hYdMbGdfU68SKaCV2spy7vq3bZWZ5lyw4Rc7ZhX5poEaLcw8rGWjnItlTIOHOZXgaWEoLYc27Xr36gvVrbYM0j9bp4S29UfY_ZH7N0UYnTvT1bNKBL7ZbdFeXYMn2DH4DShOI71k7FWzXP3wNmBkZ4iz24ux2NREaCUrBQB8kSZ1yJyxYCWrtClO4PwceJTGFzr3mSy-_g6fNWOl1ARrPjYeORZUrrwJOU5-nmr-ISD4Zw_N9z3GUba2pXNS96cKncQ"
OWNER_HEADERS = {"Authorization": f"Bearer {OWNER_TOKEN}"}

# Change this to test deleting a different item as each item can only be deleted once
ITEM_TO_DELETE = 29








# Public access test cases

def test_get_items():
    response = requests.get(f"{BASE_URL}/items")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("items"), list)

def test_get_item_by_id():
    response = requests.get(f"{BASE_URL}/items/1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("item", {}).get("id") == 1

def test_get_customers_unauthorized():
    response = requests.get(f"{BASE_URL}/customers")
    assert response.status_code == 401

def test_get_customer_unauthorized():
    response = requests.get(f"{BASE_URL}/customer")
    assert response.status_code == 401

def test_get_customer_cart_unauthorized():
    response = requests.get(f"{BASE_URL}/customer/cart")
    assert response.status_code == 401

def test_add_moonstone_studs_unauthorized():
    payload = {
        "name": "Celestial Moonstone Studs",
        "description": "Dainty moonstone stud earrings set in sterling silver.",
        "image": "celestial_moonstone_studs.jpg",
        "cost": 249.99
    }
    response = requests.post(f"{BASE_URL}/items", json=payload)
    assert response.status_code == 401

def test_create_customer_unauthorized():
    payload = {
        "image": "james_image.jpg",
        "name": "James",
        "cart": []
    }
    response = requests.post(f"{BASE_URL}/customer", json=payload)
    assert response.status_code == 401

def test_add_to_cart_unauthorized():
    response = requests.post(f"{BASE_URL}/items/3/add_to_cart")
    assert response.status_code == 401

def test_remove_from_cart_unauthorized():
    response = requests.post(f"{BASE_URL}/items/3/remove_from_cart")
    assert response.status_code == 401

def test_place_order_unauthorized():
    response = requests.post(f"{BASE_URL}/customer/place_order")
    assert response.status_code == 401

def test_patch_item_cost_unauthorized():
    payload = {"cost": 120.99}
    response = requests.patch(f"{BASE_URL}/items/7", json=payload)
    assert response.status_code == 401

def test_patch_cart_unauthorized():
    payload = {"cart": [2, 3, 8]}
    response = requests.patch(f"{BASE_URL}/customer", json=payload)
    assert response.status_code == 401

def test_delete_item_unauthorized():
    response = requests.delete(f"{BASE_URL}/items/4")
    assert response.status_code == 401

def test_delete_customer_unauthorized():
    response = requests.delete(f"{BASE_URL}/customer")
    assert response.status_code == 401














# Customer 1 test cases

def test_get_items_customer1():
    response = requests.get(f"{BASE_URL}/items", headers=CUSTOMER1_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("items"), list)

def test_get_item_by_id_customer1():
    response = requests.get(f"{BASE_URL}/items/1", headers=CUSTOMER1_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("item", {}).get("id") == 1

def test_get_customers_forbidden_customer1():
    response = requests.get(f"{BASE_URL}/customers", headers=CUSTOMER1_HEADERS)
    assert response.status_code == 403  # Customer role is not authorized

def test_get_customer_details_customer1():
    response = requests.get(f"{BASE_URL}/customer", headers=CUSTOMER1_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_get_customer_cart_customer1():
    response = requests.get(f"{BASE_URL}/customer/cart", headers=CUSTOMER1_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("cart"), list)

def test_add_to_cart_customer1():
    response = requests.post(f"{BASE_URL}/items/3/add_to_cart", headers=CUSTOMER1_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("cart"), list)

def test_remove_from_cart_customer1():
    response = requests.post(f"{BASE_URL}/items/3/remove_from_cart", headers=CUSTOMER1_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("cart"), list)

def test_place_order_customer1():
    response = requests.post(f"{BASE_URL}/customer/place_order", headers=CUSTOMER1_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_add_item_forbidden_customer1():
    payload = {
        "name": "Celestial Moonstone Studs",
        "description": "Dainty moonstone stud earrings set in sterling silver.",
        "image": "celestial_moonstone_studs.jpg",
        "cost": 249.99
    }
    response = requests.post(f"{BASE_URL}/items", json=payload, headers=CUSTOMER1_HEADERS)
    assert response.status_code == 403  # Customer1 is not authorized to add items

def test_patch_customer_info_customer1():
    payload = {"image": "bob_image_update.jpg", "name": "Bob B"}
    response = requests.patch(f"{BASE_URL}/customer", json=payload, headers=CUSTOMER1_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_patch_cart_customer1():
    payload = {"cart": [3, 7, 15, 23]}
    response = requests.patch(f"{BASE_URL}/customer", json=payload, headers=CUSTOMER1_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_patch_item_forbidden_customer1():
    payload = {"name": "Black Onyx Earrings"}
    response = requests.patch(f"{BASE_URL}/items/7", json=payload, headers=CUSTOMER1_HEADERS)
    assert response.status_code == 403  # Customer1 is not authorized to modify items

def test_delete_item_forbidden_customer1():
    response = requests.delete(f"{BASE_URL}/items/4", headers=CUSTOMER1_HEADERS)
    assert response.status_code == 403  # Customer1 is not authorized to delete items










# Customer 2 Test Cases

def test_get_items_customer2():
    response = requests.get(f"{BASE_URL}/items", headers=CUSTOMER2_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("items"), list)

def test_get_item_by_id_customer2():
    response = requests.get(f"{BASE_URL}/items/1", headers=CUSTOMER2_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("item", {}).get("id") == 1

def test_get_customers_forbidden_customer2():
    response = requests.get(f"{BASE_URL}/customers", headers=CUSTOMER2_HEADERS)
    assert response.status_code == 403  # Customer role is not authorized

def test_get_customer_details_customer2():
    response = requests.get(f"{BASE_URL}/customer", headers=CUSTOMER2_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_get_customer_cart_customer2():
    response = requests.get(f"{BASE_URL}/customer/cart", headers=CUSTOMER2_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("cart"), list)

def test_add_to_cart_customer2():
    response = requests.post(f"{BASE_URL}/items/3/add_to_cart", headers=CUSTOMER2_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("cart"), list)

def test_remove_from_cart_customer2():
    response = requests.post(f"{BASE_URL}/items/3/remove_from_cart", headers=CUSTOMER2_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("cart"), list)

def test_place_order_customer2():
    response = requests.post(f"{BASE_URL}/customer/place_order", headers=CUSTOMER2_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_add_item_forbidden_customer2():
    payload = {
        "name": "Celestial Moonstone Studs",
        "description": "Dainty moonstone stud earrings set in sterling silver.",
        "image": "celestial_moonstone_studs.jpg",
        "cost": 249.99
    }
    response = requests.post(f"{BASE_URL}/items", json=payload, headers=CUSTOMER2_HEADERS)
    assert response.status_code == 403  # Customer2 is not authorized to add items

def test_patch_customer_info_customer2():
    payload = {"image": "charlie_image_update.jpg", "name": "Charlie C"}
    response = requests.patch(f"{BASE_URL}/customer", json=payload, headers=CUSTOMER2_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_patch_cart_customer2():
    payload = {"cart": [2, 8, 12]}
    response = requests.patch(f"{BASE_URL}/customer", json=payload, headers=CUSTOMER2_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_patch_item_forbidden_customer2():
    payload = {"name": "Black Onyx Earrings"}
    response = requests.patch(f"{BASE_URL}/items/7", json=payload, headers=CUSTOMER2_HEADERS)
    assert response.status_code == 403  # Customer2 is not authorized to modify items

def test_delete_item_forbidden_customer2():
    response = requests.delete(f"{BASE_URL}/items/4", headers=CUSTOMER2_HEADERS)
    assert response.status_code == 403  # Customer2 is not authorized to delete items







# Customer 3 Test Cases

def test_add_customer_james():
    payload = {
        "cart": [1, 2, 6],
        "image": "james_image.jpg",
        "name": "James"
    }
    response = requests.post(f"{BASE_URL}/customer", json=payload, headers=CUSTOMER3_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_delete_customer_james():
    response = requests.delete(f"{BASE_URL}/customer", headers=CUSTOMER3_HEADERS)
    assert response.status_code == 200













def test_get_items_owner():
    response = requests.get(f"{BASE_URL}/items", headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("items"), list)

def test_get_item_by_id_owner():
    response = requests.get(f"{BASE_URL}/items/1", headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("item", {}).get("id") == 1

def test_get_customers_owner():
    response = requests.get(f"{BASE_URL}/customers", headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customers"), list)

def test_get_customer_owner():
    response = requests.get(f"{BASE_URL}/customer", headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_get_customer_cart_owner():
    response = requests.get(f"{BASE_URL}/customer/cart", headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("cart"), list)

def test_add_to_cart_owner():
    response = requests.post(f"{BASE_URL}/items/3/add_to_cart", headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("cart"), list)

def test_remove_from_cart_owner():
    response = requests.post(f"{BASE_URL}/items/3/remove_from_cart", headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("cart"), list)

def test_place_order_owner():
    response = requests.post(f"{BASE_URL}/customer/place_order", headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_add_moonstone_studs_owner():
    payload = {
        "name": "Celestial Moonstone Studs",
        "description": "Dainty moonstone stud earrings set in sterling silver, radiating a soft iridescence reminiscent of a moonlit night.",
        "image": "celestial_moonstone_studs.jpg",
        "cost": 249.99
    }
    response = requests.post(f"{BASE_URL}/items", json=payload, headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("item", {}).get("name") == "Celestial Moonstone Studs"

def test_add_vine_hoops_owner():
    payload = {
        "name": "Rose Gold Vine Hoops",
        "description": "Delicate rose gold hoops entwined with intricate vine detailing, adding a touch of nature-inspired elegance.",
        "image": "rose_gold_vine_hoops.jpg",
        "cost": 149.99
    }
    response = requests.post(f"{BASE_URL}/items", json=payload, headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("item", {}).get("name") == "Rose Gold Vine Hoops"

def test_patch_customer_owner():
    payload = {"image": "alice_image_update.jpg", "name": "Alice A"}
    response = requests.patch(f"{BASE_URL}/customer", json=payload, headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_patch_cart_owner():
    payload = {"cart": [2, 3, 8]}
    response = requests.patch(f"{BASE_URL}/customer", json=payload, headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data.get("customer", {}).get("cart"), list)

def test_patch_item_name_owner():
    payload = {"name": "Black Onyx Earrings"}
    response = requests.patch(f"{BASE_URL}/items/7", json=payload, headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("item", {}).get("name") == "Black Onyx Earrings"

def test_patch_item_cost_owner():
    payload = {"cost": 120.99}
    response = requests.patch(f"{BASE_URL}/items/7", json=payload, headers=OWNER_HEADERS)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("item", {}).get("cost") == 120.99

def test_delete_item_owner():
    response = requests.delete(f"{BASE_URL}/items/{ITEM_TO_DELETE}", headers=OWNER_HEADERS)
    assert response.status_code == 200







