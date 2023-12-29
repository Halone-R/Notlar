from src.business.services import NoteService

class NoteController:
    def __init__(self, note_service: NoteService):
        self.note_service = note_service

    def create_note(self, user_id, title, content):
        #Lógica para criar uma nova nota
        note_id = self.note_service.create_note(user_id, title, content)
        return {"note_id": note_id, "message": "Note created successfully"}
    
    def get_note(self, user_id, note_id):
        # Lógica para obter uma nota específica
        note = self.note_service.get_note(user_id, note_id)
        return {"note": note, "message": "Note retrieved successfully"}
    
    def update_note(self, user_id, note_id, title, content):
        # Lógica para atualizar uma nota existente
        self.note_service.update_note(user_id, note_id, title, content)
        return {"message": "Note updated successfully"}
    
    def delete_note(self, user_id, note_id):
        # Lógica para excluir uma nota existente
        self.note_service.delete_note(user_id, note_id)
        return {"message": "Note deleted successfully"}