def debugPrint(message):
    try:
        import arcpy

        arcpy.AddMessage(message)
    except Exception:
        print(message)
