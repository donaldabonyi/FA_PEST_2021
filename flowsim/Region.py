class Region:
    def __init__(self, name, position_start, position_end):
        self.name = name
        self.positionStart = position_start
        self.positionEnd = position_end
        
    def to_pflotran(self):
        return f"""
        REGION {self.name}
            COORDINATES\n" \
                {self.positionStart.to_pflotran()}
                {self.positionEnd.to_pflotran()}
            /
        END
        """