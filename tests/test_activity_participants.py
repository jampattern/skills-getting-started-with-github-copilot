from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_remove_participant_from_activity():
    activity_name = "Chess Club"
    original_participants = activities[activity_name]["participants"].copy()

    try:
        response = client.delete(
            f"/activities/{activity_name}/participants",
            params={"email": "michael@mergington.edu"},
        )

        assert response.status_code == 200
        assert "michael@mergington.edu" not in activities[activity_name]["participants"]
        assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"
    finally:
        activities[activity_name]["participants"] = original_participants
