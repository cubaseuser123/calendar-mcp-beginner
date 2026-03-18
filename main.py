from mcp.server.fastmcp import FastMCP
from typing import List, Dict
from datetime import datetime
import json
from pathlib import Path

mcp = FastMCP("EventCalendar")

DATA_FILE = Path(__file__).parent / "events.json"

def load_events() -> List[Dict]:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_events(events: List[Dict]):
    with open(DATA_FILE, "w") as f:
        json.dump(events, f, indent=2)


#adding an event 

@mcp.tool()

def add_event(title: str, date: str, description: str = "") -> str:
    """
    Add a new calendar event.
    Date format: YYYY-MM-DD
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        events = load_events()
        events.append({"title": title, "date": date, "description": description})
        save_events(events)
        return f"Event '{title}' added for {date}"
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."

#viewing events 

@mcp.tool()

def view_events() -> str:
    """
    View all calendar events.
    """
    events = load_events()
    if not events:
        return "No events scheduled."
    result = "Calendar events:\n"
    for event in sorted(events, key=lambda x: x["date"]):
        desc = f" - {event['description']}" if event['description'] else ""
        result += f"- {event['date']}: {event['title']}{desc}\n"
    return result

#delete events

@mcp.tool()

def delete_event(title : str) -> str:
    """
    Delete an event by title.
    """
    events = load_events()
    initial_length = len(events)
    events = [e for e in events if e['title'].lower() != title.lower()]
    if len(events) < initial_length:
        save_events(events)
        return f"Event '{title}' deleted."
    else:
        return f"No event found with title '{title}'."

#summarize events

@mcp.prompt()
def summarize_events() -> str:
    """
    Generate a summary of upcoming events.
    """
    events = load_events()
    if not events:
        return "No events scheduled."
    summary = "Upcoming Events Summary:\n"
    for e in sorted(events, key=lambda x: x['date']):
        summary += f"- {e['date']}: {e['title']}"
        if e['description']:
            summary += f" ({e['description']})"
        summary += "\n"
    return summary

if __name__ == "__main__":
    mcp.run()



