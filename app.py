import gradio as gr
import pandas as pd
from datetime import datetime
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Try to import pybaseball
try:
    from pybaseball import statcast_batter, statcast_pitcher, playerid_lookup
except ImportError:
    print("Warning: pybaseball not installed. Installing it now...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pybaseball"])
    from pybaseball import statcast_batter, statcast_pitcher, playerid_lookup

def get_player_id(player_name):
    """Get player ID from player name."""
    try:
        # Split the name into first and last
        name_parts = player_name.strip().split(' ')
        if len(name_parts) < 2:
            return None, f"Please provide both first and last name for {player_name}"
        
        first_name = name_parts[0]
        last_name = ' '.join(name_parts[1:])
        
        # Look up the player ID
        player_info = playerid_lookup(last_name, first_name)
        
        if player_info.empty:
            return None, f"No player found with name: {player_name}"
        
        # Get the most recent player ID (in case of multiple matches)
        player_id = player_info.iloc[0]['key_mlbam']
        return player_id, None
    except Exception as e:
        return None, f"Error looking up player: {str(e)}"

def get_player_stats(player_name, date_str):
    """Get player statistics for a specific date."""
    try:
        # Validate date format
        try:
            selected_date = datetime.strptime(date_str, "%Y-%m-%d")
            date_str = selected_date.strftime("%Y-%m-%d")
        except ValueError:
            return pd.DataFrame(), f"Invalid date format. Please use YYYY-MM-DD format."
        
        # Get player ID
        player_id, error = get_player_id(player_name)
        if error:
            return pd.DataFrame(), error
        
        # Try to get player statistics as a batter first
        stats = statcast_batter(start_dt=date_str, end_dt=date_str, player_id=player_id)
        
        # If no batter stats, try pitcher stats
        if stats.empty:
            stats = statcast_pitcher(start_dt=date_str, end_dt=date_str, player_id=player_id)
        
        if stats.empty:
            return pd.DataFrame(), f"No statistics found for {player_name} on {date_str}"
        
        # Select relevant columns for display
        display_columns = [
            'game_date', 'player_name', 'events', 'description', 
            'pitch_type', 'release_speed', 'launch_speed', 'launch_angle',
            'hit_distance_sc', 'estimated_ba_using_speedangle'
        ]
        
        # Filter columns that exist in the dataframe
        display_columns = [col for col in display_columns if col in stats.columns]
        
        return stats[display_columns], None
    except Exception as e:
        return pd.DataFrame(), f"Error retrieving statistics: {str(e)}"

def display_player_stats(player_name, date):
    """Gradio interface function to display player statistics."""
    if not player_name or not date:
        return pd.DataFrame(), "Please provide both player name and date."
    
    stats, error = get_player_stats(player_name, date)
    
    if error:
        return pd.DataFrame(), error
    
    return stats, f"Statistics for {player_name} on {date}"

# Create Gradio interface
def create_interface():
    with gr.Blocks(title="MLB Player Statistics") as app:
        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown("# MLB Player Daily Statistics")
                gr.Markdown("Enter a player's name and date to view their statistics for that day.")
            
            with gr.Column(scale=1):
                player_input = gr.Textbox(label="Player Name (First Last)", placeholder="Mike Trout")
                date_input = gr.Textbox(label="Date (YYYY-MM-DD)", placeholder="2023-07-15")
                submit_btn = gr.Button("Get Statistics")
        
        with gr.Row():
            output_message = gr.Textbox(label="Status")
        
        with gr.Row():
            output_table = gr.DataFrame(label="Player Statistics")
        
        # Add examples for quick testing
        gr.Examples(
            examples=[
                ["Mike Trout", "2023-07-15"],
                ["Aaron Judge", "2023-08-20"],
                ["Shohei Ohtani", "2023-06-10"],
                ["Clayton Kershaw", "2023-05-05"]
            ],
            inputs=[player_input, date_input]
        )
        
        submit_btn.click(
            fn=display_player_stats,
            inputs=[player_input, date_input],
            outputs=[output_table, output_message]
        )
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch(share=False)
