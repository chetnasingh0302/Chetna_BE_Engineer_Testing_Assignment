from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional
from scraper import Scraper
from database_handler import DatabaseHandler
from notification_system import NotificationSystem

app = FastAPI()

# Static token for authentication
TOKEN = "SECRET_TOKEN"

# Initialize components
scraper = Scraper()
db_handler = DatabaseHandler()
notification_system = NotificationSystem()


class Settings(BaseModel):
    pages_limit: Optional[int] = None
    proxy: Optional[str] = None


@app.post("/scrape")
async def scrape_data(settings: Settings, token: str = Header(None)):
    if token != TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")   
    try:
        scraped_data = scraper.scrape(settings.pages_limit, settings.proxy)
        updated_count = db_handler.update_database(scraped_data)
        notification_system.notify(f"{updated_count} products scraped and updated in DB")
        return {"message": "Scraping completed successfully"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
