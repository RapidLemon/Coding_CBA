using System.Diagnostics;
using UnityEngine;

public class AStarController : MonoBehaviour
{
    public GameObject character;  // The GameObject that represents the character

    void Start()
    {
        string exePath = "path/to/your/exe/file.exe";
        string arguments = "(currentPosition,targetPosition)";

        Process process = new Process();
        process.StartInfo.FileName = exePath;
        process.StartInfo.Arguments = arguments;
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.RedirectStandardOutput = true;
        process.Start();

        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();

        Debug.Log(output);

        // Parse the output string and move the character towards each position
        string[] positions = output.Trim().Split('\n');
        foreach (string pos in positions)
        {
            Vector3 targetPos = StringToVector3(pos.Trim());
            MoveCharacterTowards(targetPos);
        }
    }

    void MoveCharacterTowards(Vector3 targetPos)
    {
        // Calculate the direction and distance to move the character
        Vector3 dir = (targetPos - character.transform.position).normalized;
        float dist = Vector3.Distance(targetPos, character.transform.position);

        // Move the character towards the target position
        character.transform.position += dir * Mathf.Min(dist, Time.deltaTime * speed);
    }

    Vector3 StringToVector3(string str)
    {
        string[] parts = str.Split(',');
        float x = float.Parse(parts[0]);
        float y = float.Parse(parts[1]);
        float z = float.Parse(parts[2]);
        return new Vector3(x, y, z);
    }
}
