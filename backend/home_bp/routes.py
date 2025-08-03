from flask import Blueprint, jsonify, request, session, send_file
from pathlib import Path
from werkzeug.utils import secure_filename
import os

# importing files: 
from PythonTasks.helper import formDataHelper
from PythonTasks.Exceptions.handleExceptions import CertificateError


# Blueprint for home-page routes
home_bp = Blueprint('home', __name__, url_prefix='/home')

# -----------------------------------------------------------------------------
# CONFIG
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
PARENT_DIR = BASE_DIR.parent
UPLOAD_DIR = PARENT_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


ALLOWED_IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}
ALLOWED_CSV_EXT   = {".csv"}


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def _save_file(file_storage, subdir=""):
    """Save an uploaded FileStorage to disk and return its server path."""
    if not file_storage or not file_storage.filename:
        return None

    filename = secure_filename(file_storage.filename)
    ext = Path(filename).suffix.lower()

    # simple validation
    if ext not in ALLOWED_IMAGE_EXT and ext not in ALLOWED_CSV_EXT:
        raise ValueError(f"Unsupported file type: {filename}")

    target_dir = UPLOAD_DIR / subdir
    target_dir.mkdir(exist_ok=True)
    disk_path = target_dir / filename
    file_storage.save(disk_path)
    return str(disk_path)



 # -----------------------------------------------------------------------------
# 👇 MAIN FORM HANDLER
# -----------------------------------------------------------------------------

@home_bp.post("/FormData")
def userFormData():
    print("\n\n\n\n")
    print(f"===================================== OUR CONSOLE STARTS HERE ==========================================")
    try:
        # ---------- 1) TEXT FIELDS ----------
        text_fields = {
            "eventName":            request.form.get("eventName"),
            "organizationName":     request.form.get("organizationName"),
            "certificateType":      request.form.get("certificateType"),
            "certificate_choice":   request.form.get("certificate_choice"),
            "organizer1Desig":      request.form.get("organizer1Desig"),
            "organizer2Desig":      request.form.get("organizer2Desig"),
            "action":               request.form.get("action"),  # Preview / Generate
        }
        textValues = list(text_fields.values())

        # ---------- 2) FILES ----------
        saved_files = {
            "logo":        _save_file(request.files.get("logo"),        "logos"),
            "logo2":       _save_file(request.files.get("logo2"),       "logos"),
            "organizer1":  _save_file(request.files.get("organizer1"),  "signatures"),
            "organizer2":  _save_file(request.files.get("organizer2"),  "signatures"),
            "csv":[]
        } # ........
        filePaths = list(saved_files.values())
        filePaths.pop() # to remove last empty list from list

        # # CSV(s) – could be multiple
        csv_files = [] # ..........
        for fs in request.files.getlist("file"):
            saved_path = _save_file(fs, "csv")
            if saved_path:
                csv_files.append(saved_path)
        saved_files["csv"] = csv_files # ................

        # # ---------- 3) LOG / DEBUG ----------
        # print("\n\n⇢ Text fields:", text_fields)
        # print("\n\n⇢ Saved files :", saved_files) # .............

        # ---------- 4) TODO: CERTIFICATE GENERATION ----------
        # • Read csv_files                           → pandas / csv module
        # • For each participant, open template img  → Pillow
        # • Draw text & paste signatures             → Pillow
        # • Save PDFs / PNGs                         → output dir / maybe zip
        # • Return download link or generate ZIP     → send_file / jsonify link


        zipPath = formDataHelper(text_fields, saved_files)
        session['zipPath'] = zipPath
        print(f"\n\nAfter returning to app:\nSession is: {session['zipPath']}")

        return jsonify(
            status="ok",
            text=text_fields,
            files=saved_files, # .........
            message="Form data received – certificate generation yet to be implemented.",
        )
    
    except CertificateError as ce: # Let Flask's error‑handler catch it
        raise ce  

    except Exception as exc:
        print("❌ Unexpected Error in /api/FormData:", exc)
        return jsonify(error="Internal server error"), 500  


@home_bp.errorhandler(CertificateError)
def handle_certificate_error(e):
    print(f"\n\tEception handler called...{e.message}")
    return jsonify({"error": e.message}), 400  # or 422 (unprocessable entity)  


@home_bp.route('/download-zip', methods=['GET'])
def download_zip():
    zipPath = session.get('zipPath')
    print(f"In zipDownload...\n\tSession path: {zipPath}")
    # zip_path = f"./static/GenerateCertificate.zip"  # Absolute or relative path
    
    if not zipPath:
        return {"error": "ZIP file not prepared yet"}, 400
    
    if not os.path.exists(zipPath):
        return {"error": "ZIP file not found"}, 404
    
    print(f"\n\nIn download-zip:\nSession is: {session['zipPath']}")
    return send_file(zipPath, as_attachment=True)
