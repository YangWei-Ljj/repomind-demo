from app.services.github_sync import sync_issues


def test_sync_issues():
    items = [{"number": 1}, {"number": 2}, {"number": 3}]
    assert len(sync_issues(items)) == 3
